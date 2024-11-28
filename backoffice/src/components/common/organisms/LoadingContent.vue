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
@import "@/assets/scss/variables";

.loading-wp {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 10rem;
  span {
    animation: spin 1.5s infinite;
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
