<template>
  <img :src="src" :alt="alt" :style="imgStyle" />
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
    width: {
      type: String,
      required: true,
    },
    height: {
      type: String,
      required: true,
    },
  },
  computed: {
    imgStyle() {
      return {
        width: this.width,
        height: this.height,
      };
    },
  },
});
</script>

<style scoped></style>
