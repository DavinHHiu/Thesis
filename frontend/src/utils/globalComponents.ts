import Toast from "@/components/common/organisms/Toast.vue";
import { App } from "vue";

export default {
  install(app: App) {
    app.component("Toast", Toast);
  },
};
