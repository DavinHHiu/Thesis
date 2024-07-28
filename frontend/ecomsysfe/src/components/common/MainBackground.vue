<template>
  <div class="bg-wrapper">
    <image-slider
      :auto="true"
      class="bg-image h-[900px] w-screen"
      :slides="[{ src: '/images/1.jpg' }]"
    >
      <img class="image w-screen" src="/images/4.jpg" />
      <!-- <img class="image w-screen" src="/images/1.jpg" /> -->
    </image-slider>
    <div class="search-bar-wp"><search-bar class="search-bar" /></div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import ImageSlider from './ImageSlider.vue';
import SearchBar from './SearchBar.vue';

export default defineComponent({
  name: 'MainBackground',
  components: {
    ImageSlider,
    SearchBar,
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.bg-wrapper {
  position: relative;
  height: 90rem;
  &::after {
    position: absolute;
    top: 0;
    content: '';
    width: 100%;
    height: 100%;
    background-color: transparent;
    background-image: linear-gradient(
      180deg,
      $--color-blue 0%,
      $--primary-color 100%
    );
    opacity: 0.3;
  }
  .bg-image {
    position: fixed;
    z-index: 0;
  }
  .search-bar-wp {
    height: 5rem;
    .search-bar {
      position: absolute;
      height: 5rem;
      top: 25%;
      left: 50%;
      transform: translate(-50%, -50%);
      z-index: 2;
    }
  }
}
</style>
