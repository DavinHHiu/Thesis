<template>
  <input ref="inputRef" :type="type" />
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'RangeField',
  props: {
    type: {
      type: String,
      default: 'range',
    },
  },
  methods: {
    getInputRef() {
      return this.$refs.inputRef;
    },
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

input {
  position: absolute;
  top: -0.3rem;
  padding: 0 0;
  height: 0.3rem;
  width: 100%;
  pointer-events: none;
  background: none;
  border: none;
  -webkit-appearance: none;
  appearance: none;
}
input[type='range']::-webkit-slider-thumb {
  -webkit-appearance: none;
  height: 1.7rem;
  width: 1.7rem;
  pointer-events: auto;
  background-color: $--primary-color;
  border-radius: 50%;
}
input[type='range']::-moz-slider-thumb {
  -moz-appearance: none;
  height: 1.7rem;
  width: 1.7rem;
  pointer-events: auto;
  background-color: $--primary-color;
  border-radius: 50%;
}
</style>
