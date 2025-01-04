<template>
  <div class="container" :style="customStyle">
    <slot class="flex-item"></slot>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "GridLayout",
  props: {
    rowGap: {
      type: [Number, String],
    },
    columnGap: {
      type: [Number, String],
    },
    wrap: {
      type: String,
      default: "nowrap",
    },
    alignItems: {
      type: String,
      default: "start",
    },
    justifyConent: {
      type: String,
      default: "space-between",
    },
  },
  computed: {
    customStyle() {
      return {
        rowGap: this.rowGap ? this.rowGap + "rem" : "0rem",
        columnGap: this.columnGap ? this.columnGap + "rem" : "0rem",
        flexWrap: this.wrap || "nowrap",
        alignItems: this.alignItems,
        justifyContent: this.justifyConent,
      };
    },
  },
});
</script>
<style lang="scss" scoped>
.container {
  display: flex;
  justify-content: center;
  width: 100%;
  .flex-item {
    flex: 1 1 20rem;
  }
}
</style>
