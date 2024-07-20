<template>
  <div class="product-wrapper">
    <div class="image-wrapper w-[245px] h-[245px] mb-[10px]">
      <img
        loading="lazy"
        src="https://websitedemos.net/brandstore-02/wp-content/uploads/sites/150/2017/12/product-hoodie1-300x300.jpg"
      />
    </div>
    <div class="info-wrapper flex flex-col gap-[12px]">
      <h2 class="font-bold text-base">Black Hoodie</h2>
      <span class="text-slate-400"> Men </span>
      <span class="price font-semibold"> $150.00 </span>
      <div class="star-rating"></div>
    </div>
    <custom-button
      class="btn-add-to-cart w-full h-[50px] rounded-none"
      intent="outline"
    >
      Add to Cart
    </custom-button>
  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import CustomButton from './CustomButton.vue';

export default defineComponent({
  name: 'ProductItem',
  components: {
    CustomButton,
  },
});
</script>

<style lang="scss" scoped>
.product-wrapper {
  position: relative;
  overflow: hidden;
  cursor: pointer;

  &:hover {
    .info-wrapper {
      visibility: hidden;
      opacity: 0;
    }
    .btn-add-to-cart {
      position: absolute;
      bottom: 0;
      opacity: 100%;
    }
  }

  .info-wrapper {
    visibility: visible;
    opacity: 100%;
    transition: 0.2s ease-in-out;
  }

  .btn-add-to-cart {
    position: absolute;
    bottom: -50px;
    opacity: 0;
    transition: 0.4s ease-out;
  }
}
</style>
