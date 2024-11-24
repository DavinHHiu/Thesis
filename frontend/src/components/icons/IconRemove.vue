<template>
  <svg
    class="icon-remove"
    width="2rem"
    height="2rem"
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 64 64"
    transform="rotate(45)"
  >
    <g fill="none" :stroke="stroke" stroke-width="4" stroke-miterlimit="10">
      <path d="M32 50V14M14 32h36" />
    </g>
    <circle
      fill="none"
      :stroke="stroke"
      stroke-width="4"
      stroke-miterlimit="10"
      cx="32"
      cy="32"
      r="30.999"
    />
  </svg>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "IconRemove",
  props: {
    stroke: {
      type: String,
      default: "#aaa",
    },
  },
});
</script>

<style scoped>
.icon-remove {
  cursor: pointer;
}
</style>
