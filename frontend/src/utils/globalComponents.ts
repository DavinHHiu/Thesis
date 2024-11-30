import { App } from "vue";
import LoadingContent from "@/components/common/organisms/LoadingContent.vue";
import LoadingPage from "@/components/common/organisms/LoadingPage.vue";
import Toast from "@/components/common/organisms/Toast.vue";

export default {
  install(app: App) {
    app.component("Toast", Toast);
    app.component("LoadingContent", LoadingContent);
    app.component("LoadingPage", LoadingPage);
  },
};
