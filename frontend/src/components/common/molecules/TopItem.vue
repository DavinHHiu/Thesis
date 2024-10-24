<template>
  <div class="item-wp">
    <a class="image-wp">
      <img :src="product?.images[0]" />
    </a>
    <div class="item-info-wp flex flex-col justify-center gap-[0.5rem]">
      <a>
        <span class="product-name" v-text="product?.name" />
      </a>
      <div>
        <badge-star :rating="product?.rating as number" />
      </div>
      <span class="price font-semibold" v-text="`$${product?.prices[0]}.00`" />
    </div>
  </div>
</template>

<script lang="ts">
import { Product } from "@/types/worker";
import { defineComponent, PropType } from "vue";

import BadgeStar from "./BadgeStar.vue";

export default defineComponent({
  name: "TopItem",
  components: {
    BadgeStar,
  },
  props: {
    product: {} as PropType<Product>,
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.item-wp {
  display: flex;
  padding: 1.2rem 0;
  margin-bottom: 0.5rem;
  gap: 1rem;
  .image-wp {
    display: block;
    width: 6rem;
    height: 6rem;
  }
  .item-info-wp {
    height: 100%;
    line-height: 1.2;
    font-size: $--font-base;
    .star {
      &::after {
        content: "\2606\2606\2606\2606\2606";
        font-size: $--font-2xl;
      }
    }
    .price {
      margin-top: 0.5rem;
      font-size: $--font-md;
    }
  }
}
</style>
