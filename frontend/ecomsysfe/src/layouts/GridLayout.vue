<template>
  <div class="container" :style="gridStyle">
    <slot></slot>
  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'GridLayout',
  props: {
    width: {
      type: Number || String,
      required: false,
    },
    height: {
      type: Number || String,
      required: false,
    },
    gap: {
      type: Number || String,
      required: false,
    },
    columns: {
      type: Number || String,
      required: false,
    },
    rows: {
      type: Number || String,
      required: false,
    },
    justifyContent: {
      type: String,
      required: false,
    },
    alignContent: {
      type: String,
      required: false,
    },
    justifyItems: {
      type: String,
      required: false,
    },
    alignItems: {
      type: String,
      required: false,
    },
  },
  computed: {
    gridStyle() {
      return {
        width: this.width + 'px',
        height: this.height + 'px',
        gap: this.gap + 'px',
        gridTemplateColumns: `repeat(${this.columns || 4}, 1fr)`,
        gridTemplateRows: `repeat(${this.rows}, 1fr)`,
        justifyContent: this.justifyContent || 'center',
        alignContent: this.alignContent || 'center',
        justifyItems: this.justifyItems || 'center',
        alignItems: this.alignItems || 'center',
      };
    },
  },
});
</script>
<style scoped>
.container {
  display: grid;
}
</style>
