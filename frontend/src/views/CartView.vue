<template>
  <page-title title="cartPage.title" />
  <page-body>
    <div v-if="totalQuantity === 0" class="empty-cart">
      <div class="flex items-center gap-[1rem] px-[2rem]">
        <span class="material-symbols-outlined" v-text="'event_busy'" />
        <span v-t="'cartPage.label.empty'" />
      </div>
      <custom-button
        class="px-[3rem] py-[1.25rem] mt-[5rem] uppercase"
        intent="primary"
        v-html="$t('cartPage.btnLabel.continue')"
      />
    </div>
    <div v-else class="container flex flex-col items-end">
      <table class="list-items">
        <thead>
          <tr>
            <th></th>
            <th></th>
            <th>Product</th>
            <th>Price</th>
            <th>Quantity</th>
            <th>Subtotal</th>
            <th>
              <input
                type="checkbox"
                :checked="
                  checkoutItems.length > 0 &&
                  checkoutItems.length === cartItems.length
                "
                @change="changeAllItem"
              />
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(cartItem, index) in cartItems" :key="index">
            <td class="h-full flex items-center justify-center">
              <icon-remove width="20px" height="20px" stroke="#aaa" />
            </td>
            <td>
              <a class="image"
                ><img :src="cartItem?.product_sku?.images?.[0]"
              /></a>
            </td>
            <td class="product-name">
              <a href="" v-text="cartItem?.product?.name" />
            </td>
            <td>
              <span v-text="`$${cartItem?.product_sku?.price}.00`" />
            </td>
            <td>
              <div class="quantity flex items-center gap-[0.5rem]">
                <span
                  class="material-symbols-outlined"
                  v-text="'remove'"
                  @click="decreaseQuantity(cartItem.id as number)"
                />
                <number-field
                  class="input-quantity"
                  :value="cartItem.quantity"
                  @update:modelValue="
                    (newValue) => (cartItem.quantity = newValue)
                  "
                />
                <span
                  class="material-symbols-outlined"
                  v-text="'add'"
                  @click="
                    increaseQuantity(
                      cartItem.id as number,
                      cartItem.product_sku.quantity as number
                    )
                  "
                />
              </div>
            </td>
            <td><span v-text="`$${cartItem?.subtotal}.00`" /></td>
            <td>
              <input
                type="checkbox"
                @change="changeItem($event, index)"
                :checked="
                  checkoutItems.findIndex((i) => i.id === cartItem.id) !== -1
                "
              />
            </td>
          </tr>
        </tbody>
      </table>
      <div class="cart-totals px-[20px]">
        <h2
          class="cart-totals-title font-bold"
          v-t="'cartPage.label.subtitle'"
        />
        <table>
          <tbody>
            <tr>
              <th v-t="'cartPage.label.totalQuantity'" />
              <td data-title="Subtotal" v-text="totalQuantityCheckout" />
            </tr>
            <tr>
              <th v-t="'cartPage.label.totalAmount'" />
              <td
                class="total-amount"
                data-title="Total"
                v-text="`$${totalAmountCheckout}.00`"
              />
            </tr>
          </tbody>
        </table>
        <div class="py-[16px]">
          <custom-button
            class="rounded-none w-full py-[20px] mb-[17px]"
            intent="primary"
            v-html="$t('cartPage.btnLabel.checkout')"
            @click="navigateToCheckout"
          />
        </div>
      </div>
    </div>
  </page-body>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import NumberField from "@/components/common/molecules/NumberField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import IconRemove from "@/components/icons/IconRemove.vue";
import { useCartStore } from "@/stores/cart";
import { CartItem } from "@/types/worker";
import _ from "lodash";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "CartView",
  components: {
    TextField,
    IconRemove,
    CustomButton,
    NumberField,
    PageTitle,
    PageBody,
  },
  methods: {
    ...mapActions(useCartStore, [
      "retrieveCart",
      "listCartItems",
      "updateCartItemQuantity",
      "validateCheckoutItems",
      "setCheckoutItems",
    ]),
    async increaseQuantity(cartItemId: number, maxQuantity: number) {
      let foundItem = undefined;
      let foundAt = -1;
      _.forEach(this.cartItems, (item, index) => {
        if (item.id === cartItemId && item.quantity + 1 <= maxQuantity) {
          item.quantity++;
          item.subtotal = item.product_sku.price * item.quantity;
          foundItem = item;
          foundAt = index;
        }
      });
      if (foundItem) {
        const response = await this.updateCartItemQuantity(foundItem);
        if (response?.status !== 200) {
          this.cartItems[foundAt].quantity--;
        }
      }
    },
    async decreaseQuantity(cartItemId: number) {
      let foundItem = undefined;
      let foundAt = -1;
      _.forEach(this.cartItems, (item, index) => {
        if (item.id === cartItemId && item.quantity - 1 > 0) {
          item.quantity--;
          item.subtotal = item.product_sku.price * item.quantity;
          foundItem = item;
          foundAt = index;
        }
      });
      if (foundItem) {
        const response = await this.updateCartItemQuantity(foundItem);
        if (response?.status !== 200) {
          this.cartItems[foundAt].quantity++;
        }
      }
    },
    changeItem(event: Event, index: number) {
      const target = event.target as HTMLInputElement;
      const item = this.cartItems[index];
      let items = this.checkoutItems;
      if (target.checked) {
        if (!items.find((i) => i.id === item.id)) {
          items.push(item);
        }
      } else {
        items = items.filter((i) => i.id !== item.id);
      }
      this.setCheckoutItems(items);
    },
    changeAllItem(event: Event) {
      const target = event.target as HTMLInputElement;
      if (target.checked) {
        this.setCheckoutItems(this.cartItems);
      } else {
        this.setCheckoutItems([]);
      }
    },
    async navigateToCheckout() {
      if (this.checkoutItems.length === 0) {
        alert("Please select an item to checkout");
        return;
      }
      const response = await this.validateCheckoutItems();
      if (response.status === 200) {
        this.$router.push({ name: "checkout-form" });
      }
    },
  },
  computed: {
    ...mapState(useCartStore, ["cartItems", "totalQuantity", "checkoutItems"]),
    totalQuantityCheckout() {
      return this.checkoutItems.reduce(
        (acc, curItem) => acc + curItem.quantity,
        0
      );
    },
    totalAmountCheckout() {
      return this.checkoutItems.reduce(
        (acc, curItem) => acc + curItem.subtotal,
        0
      );
    },
  },
  async mounted() {
    await this.retrieveCart();
    await this.listCartItems();
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.container {
  table {
    width: 100%;
    margin-bottom: 2rem;
    font-size: $--font-base;
    text-align: left;
    border-collapse: separate;
    border: 1px solid $--color-border;
    thead tr th {
      font-weight: $--font-bold;
    }
    th,
    td {
      padding: 1.5rem;
    }
    tbody tr {
      td {
        border-top: 1px solid $--color-border;
        min-width: 3.2rem;
        min-height: 10.1rem;
        img {
          max-width: 7rem;
        }
      }
      .image {
        display: block;
        width: 6rem;
        height: 6rem;
        img {
          width: 100%;
          height: 100%;
          object-fit: contain;
          object-position: center;
        }
      }
      .input-quantity {
        width: 5rem;
      }
      .quantity {
        span {
          cursor: pointer;
        }
      }
    }
  }
  .cart-totals {
    width: 48%;
    border: 1px solid $--color-border;

    .cart-totals-title {
      padding: 1.4rem 2rem;
      font-size: $--font-xl;
      border-bottom: 1px solid $--color-border;
      margin: 0 -2rem 2rem;
    }
    table {
      border: none;
      tbody tr td {
        border: none;
      }
      tbody tr td,
      th {
        border-bottom: 1px solid $--color-border;
      }
    }
    .total-amount {
      font-weight: $--font-bold;
    }
  }
}
.empty-cart {
  padding: 2rem 0;
  font-size: $--font-base;
  border-top: 3px solid $--primary-color;
}
</style>
