import "./assets/main.scss";
import "./assets/css/tailwind.css";
import "bootstrap/dist/js/bootstrap";

import App from "@/App.vue";
import router from "@/router";
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

router.beforeEach(async (to, from, next) => {
  const session = useSessionStore();
  if (to.meta.requiresAuth) {
    try {
      await session.refresh();
      const isAuthenticated = session.isAuthenticated;
      if (isAuthenticated && to.path === "/login") {
        return next("/");
      }
    } catch (err) {
      localStore.bulkRemove(["token", "user"]);
      return next("/login");
    }
  }
  return next();
});

axios.interceptors.request.use(
  (config) => {
    const token = localStore.get("token");
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
