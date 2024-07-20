<template>
  <div class="slide">
    <img :src="slide.src" alt="" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'ImageSlide',
  props: {
    slide: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {};
  },
});
</script>

<style scoped>
img {
  width: 100%;
}
.slide {
  display: inline-block;
}
</style>
