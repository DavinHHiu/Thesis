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
        <span v-text="formatAmount(cartItem?.product_sku?.price)" />
      </div>
    </div>
    <div class="item-actions flex items-center">
      <span
        class="material-symbols-outlined"
        v-text="'cancel'"
        @click="handleRemoveCartItem(cartItem.id as number)"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { useCartStore } from "@/stores/cart";
import { useToastStore } from "@/stores/toast";
import { CartItem } from "@/types/worker";
import { formatCurrency } from "@/utils/currency";
import { mapActions } from "pinia";
import { defineComponent, PropType } from "vue";
import { useI18n } from "vue-i18n";

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
    ...mapActions(useToastStore, ["toast"]),
    formatCurrency,
    handleRemoveCartItem(cartItemId: number) {
      this.removeCartItem(cartItemId)
        .then((res) => {
          this.toast({
            theme: "success",
            message: "cartFolder.message.delete.success",
          });
        })
        .catch((err) => {
          this.toast({
            theme: "danger",
            message: "cartFolder.message.delete.fail",
          });
        });
    },
    formatAmount(amount: number) {
      const { locale } = useI18n();
      return this.formatCurrency(locale.value, amount);
    },
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
