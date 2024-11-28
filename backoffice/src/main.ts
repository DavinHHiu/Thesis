import App from "@/App.vue";
import "@/assets/css/tailwind.css";
import "@/assets/scss/main.scss";
import config from "@/config/config.yaml";
import router from "@/routers/routers";
import { useSessionStore } from "@/stores/session";
import globalComponents from "@/utils/globalComponents";
import i18n from "@/utils/i18n";
import localStore from "@/utils/localStorage";
import axios from "axios";
import { createPinia } from "pinia";
import { createApp } from "vue";

const app = createApp(App);

app.use(createPinia());
app.use(i18n);
app.use(router);
app.use(globalComponents);

app.config.globalProperties.$config = config;

router.beforeEach(async (to, from, next) => {
  const session = useSessionStore();
  try {
    await session.refresh();
  } catch (err) {
    localStore.bulkRemove(["token", "user"]);
    return next({ name: "login" });
  }

  if (session.isAuthenticated) {
    return ["login", "register"].includes(String(to.name))
      ? next({ name: "home" })
      : next();
  }

  if (to.meta.requiresAuth) {
    localStore.bulkRemove(["token", "user"]);
    next({ name: "login" });
  }

  return next();
});

axios.interceptors.request.use(
  (config) => {
    const token = useSessionStore().token;
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

app.mount("#app");
