<template>
  <img :src="src" :alt="alt" />
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'IconImage',
  props: {
    src: {
      type: String,
      required: true,
    },
    alt: {
      type: String,
      required: false,
      default: 'IconImage',
    },
  },
});
</script>

<style scoped></style>
