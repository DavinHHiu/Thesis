<template>
  <div
    class="wrapper"
    :class="{
      [intent]: intent,
    }"
    :style="{
      width: width + 'px',
      padding: padding,
    }"
  >
    <slot></slot>
  </div>
</template>

<script lang="ts">
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
    intent: {
      type: String,
      required: false,
      default: 'card',
      validator: (val: string) => ['card', 'form'].includes(val),
    },
  },
});
</script>

<style scoped>
.card {
  position: relative;
  box-shadow: 0 0 20px 5px rgba(0, 0, 0, 0.1);
}
.form {
  box-shadow: none;
  border: 2px solid #e2e2e2;
}
</style>
