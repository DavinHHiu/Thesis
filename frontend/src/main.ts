import "./assets/main.scss";
import "./assets/css/tailwind.css";

import i18n from "@/utils/i18n";
import axios from "axios";
import { createPinia } from "pinia";
import { createApp } from "vue";

import App from "./App.vue";
import router from "./router";
import { useSessionStore } from "./stores/session";
import localStore from "./utils/localStorage";

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
