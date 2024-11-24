import { Toast } from "@/types/frontend";
import _ from "lodash";
import { defineStore } from "pinia";

export const useToastStore = defineStore("toast", {
  state() {
    return {
      toasts: [] as Toast[],
      counter: 0,
    };
  },
  actions: {
    toast(toast: Toast) {
      const newToast = {
        ...toast,
        id: this.counter,
        autohide: toast.autohide || true,
        delay: toast.delay || 2000,
      };
      this.addToast(newToast);
    },
    addToast(toast: Toast) {
      this.toasts.push(toast);
      this.counter++;
    },
    removeToast(toastId: number) {
      const index = _.findIndex(this.toasts, (toast) => toast.id === toastId);
      if (index !== -1) {
        this.toasts.splice(index, 1);
      }
      if (this.toasts.length === 0) {
        this.counter = 0;
      }
      console.log(this.toasts.length);
    },
    clearToasts() {
      this.toasts = [];
      this.counter = 0;
    },
  },
});
