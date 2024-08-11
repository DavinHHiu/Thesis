<template>
  <div class="card">
    <slot />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Card",
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.card {
  padding: 2rem 1rem;
  background-color: $--white;
  border-radius: 0.4rem;
}
</style>
