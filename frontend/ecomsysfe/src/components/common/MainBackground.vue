<template>
  <div class="bg-wrapper" :style="bgStyle">
    <div class="bg-content">
      <div class="content">
        <h1 class="title">Super Offers For<br />Hot Summer!</h1>
        <span class="desc">20% Off On All Products</span>
        <div class="btn-wp">
          <custom-button class="btn" intent="second">SHOP NOW</custom-button>
          <custom-button class="btn" intent="outlineSecond"
            >FIND MORE</custom-button
          >
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import CustomButton from './CustomButton.vue';

export default defineComponent({
  name: 'MainBackground',
  props: {
    bgImgUrl: {
      type: String,
      required: true,
    },
  },
  components: {
    CustomButton,
  },
  computed: {
    bgStyle() {
      return {
        backgroundImage: `url(${this.bgImgUrl})`,
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
      $--color-pink 0%,
      $--primary-color 100%
    );
    opacity: 0.3;
  }
  .bg-content {
    position: absolute;
    height: 100%;
    width: 65%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: $--second-color-text;
    z-index: 10;
    .content {
      .title {
        font-size: $--font-9xl;
        font-weight: $--font-bold;
        line-height: 1.5;
      }
      .desc {
        font-size: $--font-3xl;
        font-weight: $--font-semibold;
        line-height: 3;
      }
    }
  }
  .btn-wp {
    margin-top: 3rem;
    display: flex;
    align-items: center;
    width: 100%;
    gap: 2rem;
    .btn {
      padding: 1.5rem 3.5rem;
    }
  }
}
</style>
