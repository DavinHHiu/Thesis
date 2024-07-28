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

<style lang="scss"></style>
