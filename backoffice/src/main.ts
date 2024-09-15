import App from "./App.vue";
import router from "./routers/routers";
import "@/assets/css/tailwind.css";
import "@/assets/scss/main.scss";
import i18n from "@/utils/i18n";
import { createPinia } from "pinia";
import { createApp } from "vue";

const app = createApp(App);

app.use(createPinia());
app.use(i18n);
app.use(router);

app.mount("#app");
