<template>
  <div
    class="separator"
    :style="{
      borderTop: `${thickness}px solid ${color}`,
    }"
  ></div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'SeparatorLine',
  props: {
    color: {
      type: String,
      default: '#333',
      required: true,
    },
    thickness: {
      type: Number,
      default: 3,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
.separator {
  width: 100%;
}
</style>
