import App from "./App.vue";
import yamlData from "@/locales/en.yaml";
import i18n from "@/utils/i18n";
import { createPinia } from "pinia";
import { createApp } from "vue";

console.log(yamlData);

const app = createApp(App);
app.use(createPinia());
app.use(i18n);

app.mount("#app");
