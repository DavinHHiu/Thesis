<template>
  <div class="cart-folder-wp">
    <div class="cart-folder flex flex-col w-full">
      <div class="cart-folder-header w-full flex justify-between">
        <p class="cart-title" v-t="'cartFolder.title'" />
        <span
          class="material-symbols-outlined"
          @click="$emit('close:cart-folder')"
          v-text="'close'"
        />
      </div>
      <div class="cart-folder-body flex-1">
        <span
          v-if="cart.total_quantity === 0"
          class="no-product-label w-full h-full flex items-center justify-center"
          v-t="'cartFolder.label.noProduct'"
        />
        <cart-folder-item
          v-else
          v-for="(cartItem, index) in cartItems"
          :cart-item="cartItem"
          :key="index"
        />
      </div>
      <div
        v-if="cart.total_quantity > 0"
        class="subtotal flex justify-between px-[2.2rem] py-[1.2rem]"
      >
        <span v-t="'cartFolder.label.subtotal'" />
        <span v-text="formatAmount(cart?.total_amount)" />
      </div>
      <div class="cart-folder-footer">
        <custom-button
          v-if="cart.total_quantity === 0"
          class="btn-view"
          intent="primary"
          v-html="$t('cartFolder.btnLabel.continue')"
          @click="continueShopping"
        />
        <custom-button
          v-if="cart.total_quantity > 0"
          class="btn-view"
          intent="primary"
          v-html="$t('cartFolder.btnLabel.view')"
          @click="navigateToCart"
        />
        <custom-button
          v-if="cart.total_quantity > 0"
          class="btn-view"
          intent="primary"
          v-html="$t('cartFolder.btnLabel.checkout')"
          @click="handleCheckout"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import CartFolderItem from "@/components/common/molecules/CartFolderItem.vue";
import { useCartStore } from "@/stores/cart";
import { formatCurrency } from "@/utils/currency";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";
import { useI18n } from "vue-i18n";

export default defineComponent({
  name: "CartFolder",
  components: {
    CustomButton,
    CartFolderItem,
  },
  data() {
    return {
      limit: 50,
      offset: 0,
    };
  },
  computed: {
    ...mapState(useCartStore, ["cart", "cartItems"]),
  },
  methods: {
    ...mapActions(useCartStore, [
      "retrieveCart",
      "listCartItems",
      "setCheckoutItems",
      "validateCheckoutItems",
    ]),
    formatCurrency,
    formatAmount(amount: number) {
      const { locale } = useI18n();
      return this.formatCurrency(locale.value, amount);
    },
    navigateToCart() {
      this.$emit("close:cart-folder");
      this.$router.push({ name: "cartPage" });
    },
    continueShopping() {
      this.$emit("close:cart-folder");
      this.$router.push({ name: "search" });
    },
    async handleCheckout() {
      this.setCheckoutItems(this.cartItems);
      this.$emit("close:cart-folder");
      const response = await this.validateCheckoutItems();
      if (response.status === 200) {
        this.$router.push({ name: "checkout-form" });
      }
    },
  },
  async mounted() {
    await this.retrieveCart();
    await this.listCartItems({ limit: this.limit, offset: this.offset });
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.cart-folder-wp {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: $--black-alpha-40;
  opacity: 0;
  visibility: hidden;
  cursor: pointer;
  z-index: 999;
  transition: all 0.3s ease-in-out;
  .cart-folder {
    position: absolute;
    right: -35%;
    height: 100%;
    width: 35%;
    background-color: $--second-color;
    transition: all 0.3s ease-in-out;
    .cart-folder-header {
      padding: 2rem;
      border-bottom: 1px solid $--color-border;
      .cart-title {
        font-weight: $--font-semibold;
        font-size: $--font-base;
      }
    }
    .subtotal {
      border-top: 1px solid $--color-border;
      border-bottom: 1px solid $--color-border;
      font-size: $--font-base;
      span {
        font-weight: $--font-bold;
      }
    }
    .cart-folder-body {
      padding: 2.2rem;
      .no-product-label {
        font-size: $--font-base;
      }
    }
    .cart-folder-footer {
      padding: 2.2rem;
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      .btn-view {
        width: 100%;
        padding: 1.5rem;
        text-transform: uppercase;
        font-weight: $--font-bold;
      }
    }
  }
}
</style>
