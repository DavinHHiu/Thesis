<template>
  <div class="wrapper" :class="intent">
    <slot></slot>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'CardView',
  props: {
    intent: {
      type: String,
      required: false,
      default: 'card',
      validator: (val: string) => ['card', 'form'].includes(val),
    },
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.card {
  position: relative;
  background-color: $--second-color;
  box-shadow: 0 0 2rem 0.5rem $--gray-color-200;
}
.form {
  box-shadow: none;
  border: 2px solid $--color-border;
}
</style>
