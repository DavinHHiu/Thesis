// import bootstrap from ".node_modules/bootstrap/dist/js/bootstrap.js";
import App from "./App.vue";
import router from "./routers/routers";
import "@/assets/css/tailwind.css";
import "@/assets/scss/main.scss";
// import yamlData from "@/locales/en.yaml";
import i18n from "@/utils/i18n";
// import "bootstrap/dist/css/bootstrap.css";
import { createPinia } from "pinia";
import { createApp } from "vue";

// console.log(yamlData);

const app = createApp(App);
app.use(createPinia());
app.use(i18n);
// app.use(bootstrap);
app.use(router);

app.mount("#app");
