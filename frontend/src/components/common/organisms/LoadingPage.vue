<template>
  <div class="loading-wp">
    <span class="material-symbols-outlined" v-text="'hourglass_top'" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "LoadingContent",
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.loading-wp {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  background-color: $--white-alpha-70;
  transition: all 0.2s ease-out;
  z-index: 999;
  span {
    animation: spin 1.5s infinite;
  }
  .material-symbols-outlined {
    font-size: $--font-7xl;
    user-select: none;
  }
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
