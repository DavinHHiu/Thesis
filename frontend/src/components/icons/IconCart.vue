<template>
  <div class="wrapper">
    <span class="material-symbols-outlined" v-text="'shopping_cart'" />
    <div v-if="totalQuantity > 0" class="cart-quantity-wrapper">
      <p class="cart-quantity" v-text="totalQuantity" />
    </div>
  </div>
</template>

<script lang="ts">
import { useCartStore } from "@/stores/cart";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "IconCart",
  props: {
    intent: {
      type: String,
      default: "primary",
      validator: (value: string) => ["primary", "second"].includes(value),
    },
  },
  computed: {
    ...mapState(useCartStore, ["totalQuantity"]),
  },
  methods: {
    ...mapActions(useCartStore, ["retrieveCart"]),
  },
  async mounted() {
    await this.retrieveCart();
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.wrapper {
  position: relative;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  justify-content: center;
  align-items: center;

  .cart-quantity-wrapper {
    position: absolute;
    top: -0.5rem;
    right: -0.7rem;
    width: 1.5rem;
    height: 1.5rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;

    .cart-quantity {
      font-size: $--font-3xs;
      font-weight: bold;
    }
  }
}

.primary {
  .cart-quantity-wrapper {
    background-color: $--primary-color;
    .cart-quantity {
      color: $--second-color;
    }
  }
  svg path {
    fill: $--primary-color;
  }
}

.second {
  .cart-quantity-wrapper {
    background-color: $--second-color;
    .cart-quantity {
      color: $--primary-color;
    }
  }
  svg path {
    fill: $--second-color;
  }
}
</style>
