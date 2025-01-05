<template>
  <div class="badge-wp">
    <div class="badge-bg">
      <span
        class="badge-item"
        v-for="(color, index) in colors"
        :key="index"
        :style="{ backgroundColor: color.toLowerCase() }"
      ></span>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "BadgeColor",
  props: {
    colors: {
      type: Array<String>,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.badge-wp {
  position: relative;
  display: inline-block;
  .badge-bg {
    color: $--gray-color-200;
  }
  .badge-item {
    display: inline-block;
    width: 1.5rem;
    height: 1.5rem;
    border-radius: 50%;
    margin-right: 0.5rem;
  }
}
</style>
