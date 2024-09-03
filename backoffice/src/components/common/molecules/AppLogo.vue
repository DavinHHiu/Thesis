<template>
  <div class="logo-wrap h-full flex items-center">
    <span class="material-symbols-outlined icon flex items-center">sell</span>
    <span class="app-name">Price tag</span>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "AppLogo",
  props: {
    intent: {
      type: String,
      default: "primary",
    },
  },
  components: {},
});
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Rubik+Glitch&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Playwrite+CU:wght@100..400&display=swap");
@import "@/assets/scss/variables";

.app-name {
  font-family: "Playwrite CU", cursive;
  font-weight: $--font-bold;
  text-transform: uppercase;
}

.icon {
  font-size: 2.7rem;
}
</style>
