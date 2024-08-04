<template>
  <div class="wrapper">
    <slot></slot>
    <div class="info-wrapper">
      <div class="category-title">{{ title }}</div>
      <div class="category-desc">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ac
        dictum.
      </div>
      <custom-button
        class="py-[15px] px-[30px] grow-0 max-w-[145px]"
        intent="second"
        >SHOP NOW</custom-button
      >
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import CustomButton from './atomic/CustomButton.vue';

export default defineComponent({
  name: 'CategoryItem',
  components: {
    CustomButton,
  },
  props: {
    gridColumns: {
      type: Number,
      default: 1,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.wrapper {
  position: relative;
  width: 38rem;
  height: 48rem;
  &::after {
    content: '';
    display: block;
    position: absolute;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: $--black-alpha-50;
    z-index: 1;
  }

  .info-wrapper {
    position: absolute;
    bottom: 0;
    display: flex;
    flex-direction: column;
    gap: 2rem;
    color: $--second-color-text;
    padding: 4rem;
    z-index: 2;

    .category-title {
      font-size: $--font-3xl;
      font-weight: $--font-bold;
    }
    .category-desc {
      line-height: 2;
    }
  }
}
</style>
