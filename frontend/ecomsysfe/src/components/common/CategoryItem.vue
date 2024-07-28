<template>
  <div class="wrapper">
    <img
      src="https://media.wired.com/photos/624df21cb340f55b37084fdc/1:1/w_1544,h_1544,c_limit/How-to-Build-a-PC-Gear.jpg"
      class="background-image"
    />
    <div class="info-wrapper">
      <div class="category-title">Deals in PCs</div>
      <div class="category-desc">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ac
        dictum.
      </div>
      <custom-button
        class="rounded-none py-[13px] px-[30px] grow-0 max-w-[145px]"
        intent="second"
        >SHOP NOW</custom-button
      >
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import CustomButton from './CustomButton.vue';

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

  .background-image {
    position: absolute;
    top: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
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
  }
}
</style>
