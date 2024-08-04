<template>
  <div class="product-wrapper">
    <div class="image-wrapper w-[245px] h-[245px] mb-[10px]">
      <img
        loading="lazy"
        src="https://websitedemos.net/brandstore-02/wp-content/uploads/sites/150/2017/12/product-hoodie1-300x300.jpg"
      />
    </div>
    <div class="info-wrapper flex flex-col gap-[12px]">
      <p class="product-name">Black Hoodie</p>
      <span class="product-category"> Men </span>
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
import CustomButton from '../atomic/CustomButton.vue';

export default defineComponent({
  name: 'ProductItem',
  components: {
    CustomButton,
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.product-wrapper {
  position: relative;
  overflow: hidden;
  cursor: pointer;

  .product-name {
    font-size: $--font-base;
    font-weight: $--font-bold;
  }

  .product-category {
    color: $--gray-color-700;
  }

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
    bottom: -5rem;
    opacity: 0;
    transition: 0.4s ease-out;
  }
}
</style>
