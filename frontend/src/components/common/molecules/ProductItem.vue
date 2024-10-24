<template>
  <div class="product-wrapper">
    <div class="image-wrapper mb-[1rem]">
      <img class="first-img" :src="product?.images[0]" />
      <img class="second-img" :src="product?.images[1]" />
    </div>
    <div class="info-wrapper flex flex-col">
      <span class="product-name" v-text="product?.name" />
      <span class="product-category" v-text="product?.categories[0]" />
      <div>
        <badge-star :rating="product?.rating as number" />
      </div>
      <span class="price font-semibold" v-text="`$${product?.prices[0]}.00`" />
    </div>
    <custom-button
      v-text="$t('inputLabel.common.detail')"
      intent="p-outline"
      class="btn-add-to-cart w-full h-[4.5rem]"
      @click="navigateToDetail"
    />
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
  methods: {
    navigateToDetail() {
      this.$router.push({
        name: "product.detail",
        params: { id: this.product?.id },
      });
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.product-wrapper {
  width: 32%;
  position: relative;
  overflow: hidden;
  cursor: pointer;

  .image-wrapper {
    position: relative;
    width: 100%;
    padding-top: 120%;
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
    z-index: 2;
  }

  .second-img {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 1;
  }

  .product-name {
    font-size: $--font-base;
    font-weight: $--font-bold;
    text-transform: uppercase;
  }

  .product-category {
    color: $--gray-color-500;
    text-transform: uppercase;
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
    .price {
      margin-top: 0.5rem;
      font-size: $--font-md;
    }
  }

  .btn-add-to-cart {
    position: absolute;
    bottom: -5rem;
    opacity: 0;
    transition: 0.4s ease-out;
  }
}
</style>
