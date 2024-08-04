<template>
  <div class="separator"></div>
  <div class="checkout-cont">
    <div class="bill-cont">
      <div class="bill-form-cont">
        <h2 class="sub-title">Billing details</h2>
        <div class="bill-form">
          <div class="input-name-cont">
            <div class="w-full">
              <custom-label :required="true">First name</custom-label>
              <text-field class="h-[4.5rem]" :required="true" />
            </div>
            <div class="w-full">
              <custom-label :required="true">Last name</custom-label>
              <text-field class="h-[4.5rem]" :required="true" />
            </div>
          </div>
          <div>
            <custom-label>Company name (optional)</custom-label>
            <text-field class="h-[4.5rem]" :required="false" />
          </div>
          <div>
            <custom-label :required="true">Country / Region</custom-label>
            <text-field class="h-[4.5rem]" :required="true" />
          </div>
          <div>
            <custom-label :required="true">Street address</custom-label>
            <text-field
              class="h-[4.5rem]"
              :required="true"
              placeholder="House number and street name"
            />
          </div>
          <div>
            <custom-label>Postcode / ZIP (optional)</custom-label>
            <text-field class="h-[4.5rem]" :required="false" />
          </div>
          <div>
            <custom-label :required="true">Town / City</custom-label>
            <text-field class="h-[4.5rem]" :required="true" />
          </div>
          <div>
            <custom-label :required="true">Phone</custom-label>
            <text-field class="h-[4.5rem]" :required="true" />
          </div>
          <div>
            <custom-label :required="true">Email address</custom-label>
            <text-field class="h-[4.5rem]" :required="true" />
          </div>
        </div>
      </div>
      <div class="note-cont">
        <h2 class="sub-title">Additional information</h2>
        <div class="bill-form">
          <div>
            <custom-label>Order notes (optional)</custom-label>
            <text-field class="h-[4.5rem]" :required="false" />
          </div>
        </div>
      </div>
    </div>
    <div class="order-cont">
      <card-view intent="form" class="py-[2.8rem] px-[3.2rem]">
        <div class="order-title">Your order</div>
        <table class="total-cont">
          <thead>
            <tr>
              <th class="product-name">Product</th>
              <th class="product-total">Subtotal</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="product-name">Blue Denim Jeans × 1</td>
              <td class="product-total">$150.00</td>
            </tr>
          </tbody>
          <tfoot>
            <tr>
              <th class="product-name">Subtotal</th>
              <td class="product-total">$150.00</td>
            </tr>
            <tr>
              <th class="product-name">Total</th>
              <td class="product-total">$150.00</td>
            </tr>
          </tfoot>
        </table>
        <div class="payment-method-cont">
          <radio-field label="Direct bank transfer" name="payment-method" />
          <radio-field label="Check payments" name="payment-method" />
          <radio-field label="Cash on delivery" name="payment-method" />
          <div class="payment-input-cont">
            <radio-field label="PayPal" name="payment-method" />
            <img
              src="https://www.paypalobjects.com/webstatic/mktg/logo/AM_mc_vs_dc_ae.jpg"
              alt="PayPal acceptance mark"
            />
          </div>
        </div>
        <custom-button
          intent="primary"
          class="rounded-none w-full py-[16px] px-[28px]"
          >PLACE ORDER</custom-button
        >
      </card-view>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import TextField from '../components/common/molecules/TextField.vue';
import CardView from '../components/common/CardView.vue';
import CustomButton from '../components/common/atomic/CustomButton.vue';
import RadioField from '../components/common/RadioField.vue';
import CustomLabel from '../components/common/atomic/CustomLabel.vue';

export default defineComponent({
  name: 'CheckoutFormView',
  components: {
    TextField,
    CardView,
    CustomButton,
    RadioField,
    CustomLabel,
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.separator {
  width: 100%;
  border-top: 3px solid $--black-color-800;
  margin-bottom: 3.2rem;
}
.checkout-cont {
  display: flex;
  justify-content: space-between;

  .bill-cont {
    width: 55%;
    margin-bottom: 3rem;
    .sub-title {
      padding: 2rem 0 1.4rem;
      margin-bottom: 2rem;
      border-bottom: 1px solid $--color-border;
    }
    .bill-form {
      display: flex;
      flex-direction: column;
      gap: 2rem;
      width: 100%;
      .input-name-cont {
        width: 100%;
        display: flex;
        gap: 4.5rem;
      }
    }
  }
  .order-cont {
    width: 40%;
    .order-title {
      font-size: $--font-lg;
      font-weight: $--font-bold;
      padding-bottom: 2rem;
    }
    .total-cont {
      width: 100%;
      font-size: $--font-base;
      thead tr th {
        font-weight: $--font-bold;
      }
      tr {
        border-bottom: 1px solid $--color-border;
      }
      th {
        padding: 1.4rem 1.2rem 1.4rem 0;
      }
      td {
        padding: 1rem 1rem 1rem 0;
      }
      .product-name {
        text-align: left;
      }
      .product-total {
        text-align: right;
      }
    }
    .payment-method-cont {
      color: $--primary-color-text;
      margin-top: 4rem;
      display: flex;
      flex-direction: column;
      font-size: $--font-base;
      gap: 1.5rem;
      margin-bottom: 2.5rem;
      .payment-input-cont {
        display: flex;
        align-items: center;
        gap: 2rem;
        img {
          height: 5rem;
          width: auto;
        }
      }
    }
  }
}
</style>
