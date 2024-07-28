<template>
  <div>
    <div class="py-[50px] flex justify-center">
      <div class="container">
        <div>
          <h1 class="text-6xl text-center">Cart</h1>
        </div>
      </div>
    </div>
    <div class="flex justify-center">
      <div class="container flex flex-col items-end">
        <table class="list-items">
          <thead>
            <tr>
              <th></th>
              <th></th>
              <th>Product</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Subtotal</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="h-full flex items-center justify-center">
                <icon-remove width="20px" height="20px" stroke="#aaa" />
              </td>
              <td>
                <a>
                  <img
                    src="https://websitedemos.net/brandstore-02/wp-content/uploads/sites/150/2017/12/product-hoodie1-300x300.jpg"
                  />
                </a>
              </td>
              <td class="product-name">
                <a
                  href="https://websitedemos.net/brandstore-02/product/black-hoodie/"
                  >Black Hoodie</a
                >
              </td>
              <td>
                <span>$150.00</span>
              </td>
              <td>
                <div class="quantity">
                  <text-field
                    type="number"
                    class="input-quantity w-[60px] border py-[5px]"
                    value="1"
                    min="0"
                  />
                </div>
              </td>
              <td>
                <span>$150.00</span>
              </td>
            </tr>
          </tbody>
        </table>
        <div class="cart-totals px-[20px]">
          <h2 class="cart-totals-title font-bold">Cart totals</h2>
          <table cellspacing="0" class="shop_table shop_table_responsive">
            <tbody>
              <tr class="cart-subtotal">
                <th>Subtotal</th>
                <td data-title="Subtotal">$300.00</td>
              </tr>
              <tr class="order-total">
                <th>Total</th>
                <td data-title="Total">$300.00</td>
              </tr>
            </tbody>
          </table>
          <div class="py-[16px]">
            <custom-button
              class="rounded-none w-full py-[20px] mb-[17px]"
              intent="primary"
              >CHECKOUT</custom-button
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import TextField from '../components/common/TextField.vue';
import IconRemove from '../components/icons/IconRemove.vue';
import CustomButton from '../components/common/CustomButton.vue';

export default defineComponent({
  name: 'CartView',
  components: {
    TextField,
    IconRemove,
    CustomButton,
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.container {
  width: 120rem;
  max-width: 100%;

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
      .input-quantity {
        padding: 0.5rem;
        text-align: center;
        transition: 0.2s linear;
        &:focus {
          border: 1px dotted $--black-color-800;
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
  }
}
</style>
