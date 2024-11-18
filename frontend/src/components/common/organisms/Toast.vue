<template>
  <div class="toast-container">
    <div
      v-for="toast in displayToasts"
      :id="`toast-${toast.id}`"
      class="toast"
      role="alert"
      aria-live="assertive"
      aria-atomic="true"
      :data-bs-autohide="toast?.autohide"
    >
      <div class="toast-body" :class="`toast-${toast.theme}`">
        <span class="material-symbols-outlined" v-text="toast?.icon" />
        <span class="message" v-text="toast.message" />
        <span
          class="material-symbols-outlined close-btn"
          v-text="'cancel'"
          data-bs-dismiss="toast"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { useToastStore } from "@/stores/toast";
import { Toast as ToastType } from "@/types/frontend";
import { Toast } from "bootstrap";
import _ from "lodash";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "Toast",
  data() {
    return {
      displayToasts: [] as ToastType[],
    };
  },
  computed: {
    ...mapState(useToastStore, ["toasts"]),
  },
  methods: {
    ...mapActions(useToastStore, ["removeToast"]),
  },
  watch: {
    toasts: {
      handler(newToasts) {
        if (newToasts.length > this.displayToasts.length) {
          // console.log(newToasts);
          this.$nextTick(() => {
            this.displayToasts.forEach((toast) => {
              const toastElement = document.getElementById(
                `toast-${toast.id}`
              ) as HTMLElement;
              Toast.getInstance(toastElement) ?? new Toast(toastElement).show();
              toastElement.addEventListener("hidden.bs.toast", (event) => {
                const target = event.target as HTMLElement;
                this.removeToast(Number(target.id));
                target.remove();
              });
            });
          });
          this.displayToasts = _.cloneDeep(newToasts);
        }
      },
      immediate: true,
      deep: true,
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.close-btn {
  cursor: pointer;
}

.material-symbols-outlined {
  font-weight: 200;
  font-size: $--font-base;
}

.toast-success {
  color: $--color-success;
  border: 1px solid $--color-success;
}

.toast-warning {
  color: $--color-warning;
  border: 1px solid $--color-warning;
}

.toast-danger {
  color: $--color-danger;
  border: 1px solid $--color-danger;
}

.toast-info {
  color: $--color-info;
  border: 1px solid $--color-info;
}
</style>
