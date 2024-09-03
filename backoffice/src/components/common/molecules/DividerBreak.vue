<template>
  <div class="divider-wraper flex justify-center">
    <p class="title">
      {{ title }}
    </p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "DividerBreak",
  props: {
    title: {
      type: String,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.divider-wraper {
  position: relative;
  .title {
    position: relative;
    color: $--gray-color-500;
    font-size: $--font-3xs;
    display: inline-block;
    padding: 0 0.8rem 0 0.7rem;
    background-color: $--white;
    z-index: 2;
  }
  &::after {
    content: "";
    position: absolute;
    background-color: transparent;
    top: 50%;
    display: block;
    width: 100%;
    border-top: 1px solid $--dark-alt;
    z-index: 1;
  }
}
</style>
