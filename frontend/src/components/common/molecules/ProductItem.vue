<template>
  <div class="product-wrapper">
    <div class="image-wrapper mb-[1rem] w-[40rem] h-[50rem]">
      <img
        class="first-img"
        src="https://pos.nvncdn.com/778773-105877/ps/20221013_n6HKsuzizp6K2vDgrJLI4qA8.jpg"
      />
      <img
        class="second-img"
        src="https://websitedemos.net/brandstore-02/wp-content/uploads/sites/150/2017/12/product-hoodie1-300x300.jpg"
      />
    </div>
    <div class="info-wrapper flex flex-col gap-[0.7rem]">
      <span class="product-name">Black Hoodie</span>
      <span class="product-category"> Men </span>
      <div>
        <badge-star :rating="3" />
      </div>
      <span class="price font-semibold"> $150.00 </span>
    </div>
    <custom-button class="btn-add-to-cart w-full h-[4rem]" intent="p-outline">
      Add to Cart
    </custom-button>
  </div>
</template>
<script lang="ts">
import { Product } from "@/types/worker";
import { defineComponent, PropType } from "vue";

import CustomButton from "../atomic/CustomButton.vue";
import BadgeStar from "./BadgeStar.vue";

export default defineComponent({
  name: "ProductItem",
  props: {
    product: {} as PropType<Product>,
  },
  components: {
    BadgeStar,
    CustomButton,
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.product-wrapper {
  position: relative;
  overflow: hidden;
  cursor: pointer;

  .image-wrapper {
    position: relative;
  }

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: 0.2s ease-out;
  }

  .first-img {
    position: absolute;
    top: 0;
    left: 0;
    opacity: 1;
  }

  .product-name {
    font-size: $--font-base;
    font-weight: $--font-bold;
    text-transform: uppercase;
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
    .first-img {
      opacity: 0;
    }
  }

  .image-wrapper {
    overflow: hidden;
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
