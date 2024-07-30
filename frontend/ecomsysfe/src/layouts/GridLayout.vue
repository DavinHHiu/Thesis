<template>
  <div class="container" :style="customStyle">
    <slot class="flex-item"></slot>
  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'GridLayout',
  props: {
    gap: {
      type: [Number, String],
      default: '2',
    },
    wrap: {
      type: String,
      default: 'nowrap',
    },
  },
  computed: {
    customStyle() {
      return {
        gap: this.gap + 'rem',
        flexWrap: this.wrap,
      };
    },
  },
});
</script>
<style lang="scss" scoped>
.container {
  display: flex;
  justify-content: center;
  .flex-item {
    flex: 1 1 20rem;
  }
}
</style>
