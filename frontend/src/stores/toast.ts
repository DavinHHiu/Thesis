import { Toast } from "@/types/frontend";
import _ from "lodash";
import { defineStore } from "pinia";

export const useToastStore = defineStore("toast", {
  state() {
    return {
      toasts: [] as Toast[],
      counter: 0,
      themeMapIcon: {
        green: "check_circle",
        yellow: "warning",
        red: "error",
        default: "info",
      },
    };
  },
  actions: {
    toast(toast: Toast) {
      toast.id = this.counter;
      const theme = toast.theme as keyof typeof this.themeMapIcon;
      toast.icon = this.themeMapIcon[theme];
      toast.autohide ??= true;
      this.addToast(toast);
    },
    addToast(toast: Toast) {
      this.toasts.push(toast);
      this.counter++;
    },
    removeToast(toastId: number) {
      this.toasts = _.filter(this.toasts, (toast) => toast.id !== toastId);
      if (this.toasts.length === 0) {
        this.counter = 0;
      }
    },
  },
});
