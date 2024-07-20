<template>
  <div
    class="wrapper"
    :style="{
      width: width + 'px',
      padding: padding,
    }"
  >
    <slot></slot>
  </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'CardView',
  props: {
    width: {
      type: [String, Number],
      default: '100%',
      required: false,
    },
    padding: {
      type: [String, Number],
      required: false,
    },
  },
});
</script>

<style scoped>
.wrapper {
  position: relative;
  box-shadow: 0 0 20px 5px rgba(0, 0, 0, 0.1);
}
</style>
