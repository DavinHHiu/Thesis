import LoadingContent from "@/components/common/organisms/LoadingContent.vue";
import Toast from "@/components/common/organisms/Toast.vue";
import { App } from "vue";

export default {
  install(app: App) {
    app.component("Toast", Toast);
    app.component("LoadingContent", LoadingContent);
  },
};
