<template>
  <div class="item-wp flex items-center gap-[1.5rem]">
    <div class="item-image">
      <img :src="cartItem?.product_sku?.images?.[0]" alt="Item Image" />
    </div>
    <div class="item-info flex-1">
      <p class="item-name" v-text="cartItem?.product?.name" />
      <div class="item-price">
        <span v-text="cartItem?.quantity" />
        <span v-text="' x '" />
        <span v-text="`$${cartItem?.product_sku?.price}.00`" />
      </div>
    </div>
    <div class="item-actions flex items-center">
      <span
        class="material-symbols-outlined"
        v-text="'cancel'"
        @click="removeCartItem(cartItem?.id as number)"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { useCartStore } from "@/stores/cart";
import { CartItem } from "@/types/worker";
import { mapActions } from "pinia";
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "CartFolderItem",
  props: {
    cartItem: {
      type: Object as PropType<CartItem>,
      required: true,
    },
  },
  methods: {
    ...mapActions(useCartStore, ["removeCartItem"]),
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.item-wp {
  border-bottom: 1px solid $--color-border;
  &:last-child {
    border-bottom: none;
  }
  .item-image {
    width: 6rem;
    height: 6rem;
    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center;
    }
  }
  .item-info {
    padding: 1.5rem;
    .item-name {
      font-weight: $--font-semibold;
      font-size: $--font-base;
      margin-bottom: 0.5rem;
    }
    .item-price {
      font-size: $--font-base;
    }
  }
  .item-actions {
    color: $--gray-color-300;
  }
}
</style>
