<template>
  <div class="slides">
    <div class="slide-track">
      <img v-for="(x, key) in images" :key="key" :src="x.src" />
    </div>
    <div class="slide-track">
      <img v-for="(x, key) in images" :key="key" :src="x.src" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'LogoSlider',
  data() {
    return {
      images: [
        { src: '/images/brand_logos/1.jpeg' },
        { src: '/images/brand_logos/2.jpeg' },
        { src: '/images/brand_logos/3.jpeg' },
        { src: '/images/brand_logos/4.jpeg' },
        { src: '/images/brand_logos/5.jpeg' },
        { src: '/images/brand_logos/6.jpeg' },
        { src: '/images/brand_logos/7.jpeg' },
        { src: '/images/brand_logos/8.jpeg' },
        { src: '/images/brand_logos/9.jpeg' },
        { src: '/images/brand_logos/10.jpeg' },
      ],
    };
  },
});
</script>

<style lang="scss">
@import '@/assets/variables';

.slides {
  position: relative;
  margin: 10rem auto;
  display: flex;
  width: 120rem;
  overflow: hidden;
  background-color: $--second-color;
  .slide-track {
    display: flex;
    width: 240rem;
    animation: 7s linear slide infinite;
    img {
      height: 8rem;
      min-width: 12rem;
      margin: 0 4rem;
      object-fit: contain;
      object-position: center;
    }
  }
  &::before,
  &::after {
    top: 0;
    position: absolute;
    content: '';
    height: 100%;
    width: 15rem;
    z-index: 2;
  }
  &::before {
    left: 0;
    background-image: linear-gradient(
      to right,
      $--second-color,
      $--white-alpha-10
    );
  }
  &::after {
    right: 0;
    background-image: linear-gradient(
      to left,
      $--second-color,
      $--white-alpha-10
    );
  }
  &:hover .slide-track {
    animation-play-state: paused;
  }
}

@keyframes slide {
  from {
    transform: translateX(0);
  }
  to {
    transform: translateX(-100%);
  }
}
</style>
