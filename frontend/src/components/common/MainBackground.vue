<template>
  <div class="bg-wrapper" :style="bgStyle">
    <slot></slot>
  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'MainBackground',
  props: {
    bgImgUrl: {
      type: String,
      required: true,
    },
    gradientColor: {
      type: String,
    },
  },
  components: {},
  computed: {
    bgStyle() {
      return {
        backgroundImage: `url(${this.bgImgUrl})`,
        '--gradient-color': this.gradientColor,
      };
    },
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.bg-wrapper {
  position: relative;
  height: 100%;
  max-height: 47vw;
  background-attachment: fixed;
  background-position: top;
  background-repeat: none;
  background-size: cover;
  overflow: hidden;
  &::after {
    position: absolute;
    top: 0;
    content: '';
    width: 100%;
    height: 100%;
    background-color: transparent;
    background-image: linear-gradient(
      180deg,
      var(--gradient-color) 0%,
      $--primary-color 100%
    );
    opacity: 0.3;
  }
}
</style>
