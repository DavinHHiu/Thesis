<template>
  <label class="custom-label" :class="{ required: required }">
    <slot></slot>
  </label>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'CustomLabel',
  props: {
    required: {
      type: Boolean,
      default: false,
    },
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.required {
  &::after {
    content: '*';
    margin-left: 0.3rem;
    color: $--color-red;
  }
}
</style>
