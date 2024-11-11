import "./assets/main.scss";
import "./assets/css/tailwind.css";
import "bootstrap/dist/js/bootstrap";

import App from "./App.vue";
import axios from "axios";
import { createApp } from "vue";
import { createPinia } from "pinia";
import i18n from "@/utils/i18n";
import localStore from "./utils/localStorage";
import router from "./router";
import { useSessionStore } from "./stores/session";

const app = createApp(App);

app.use(createPinia());
app.use(i18n);
app.use(router);

const session = useSessionStore();

router.beforeEach(async (to, from, next) => {
  if (to.meta.requiresAuth) {
    try {
      await session.refresh();
    } catch (err) {
      localStore.bulkRemove(["token", "user"]);
      return next("/login");
    }
  }
  const isAuthenticated = session.isAuthenticated;
  if (isAuthenticated && to.path === "/login") {
    return next("/");
  }
  next();
});

axios.interceptors.request.use(
  (config) => {
    config.headers["Authorization"] = localStore.get("token");
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

app.mount("#app");
