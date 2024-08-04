<template>
  <div class="slides">
    <div
      :style="{
        width: slideInnerWidth + 'px',
        marginLeft: '-' + slidesInnerMarginLeft + 'px',
      }"
      class="slides-inner"
    >
      <slot></slot>
    </div>
    <template v-if="!auto">
      <div
        class="navigation left"
        :class="{ 'haft-navigattion': haft }"
        @click="goToPrev"
      >
        <icon-left-arrow />
      </div>
      <div
        class="navigation right"
        :class="{ 'haft-navigattion': haft }"
        @click="goToNext"
      >
        <icon-right-arrow />
      </div>
    </template>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import IconLeftArrow from '../icons/IconLeftArrow.vue';
import IconRightArrow from '../icons/IconRightArrow.vue';

export default defineComponent({
  name: 'ImageSlider',
  components: {
    IconLeftArrow,
    IconRightArrow,
  },
  data() {
    return {
      slideInnerWidth: 0,
      singleWidth: 0,
      currentIndex: 0,
      intervalId: null,
    };
  },
  props: {
    itemsPerSlide: {
      type: Number,
      default: 1,
    },
    slides: {
      type: Array,
      default: () => [],
    },
    haft: {
      type: Boolean,
      default: false,
      required: false,
    },
    title: {
      type: String,
      required: false,
    },
    auto: {
      type: Boolean,
      default: false,
      required: false,
    },
  },
  methods: {
    goToPrev() {
      this.currentIndex > 0
        ? this.currentIndex--
        : (this.currentIndex = this.slides.length - 1);
    },
    goToNext() {
      this.currentIndex < this.slides.length - 1
        ? this.currentIndex++
        : (this.currentIndex = 0);
    },
    goToSlideIndex(index: Number) {
      this.currentIndex = index;
    },
  },
  computed: {
    slidesInnerMarginLeft() {
      return this.currentIndex * this.singleWidth;
    },
  },
  mounted() {
    this.singleWidth = this.$el.clientWidth / this.itemsPerSlide;
    this.slideInnerWidth = this.singleWidth * this.slides.length;
    if (this.auto) {
      this.intervalId = window.setInterval(() => {
        this.goToNext();
      }, 5000);
    }
  },
  beforeUnmount() {
    if (this.auto) {
      clearInterval(this.intervalId);
    }
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.slides {
  position: relative;
  overflow: hidden;
  .slides-inner {
    display: inline-block;
    height: 100%;
    display: flex;
    align-items: center;
    transition: margin 0.5s ease-out;
  }
  .navigation {
    top: 0;
    position: absolute;
    height: 100%;
    width: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: $--white-alpha-20;
    cursor: pointer;
  }
  .left {
    left: 0;
  }
  .right {
    right: 0;
  }
  .haft-navigattion {
    top: 50%;
    height: 50%;
    transform: translateY(-50%);
    border-radius: 0.4rem;
  }
}
</style>
