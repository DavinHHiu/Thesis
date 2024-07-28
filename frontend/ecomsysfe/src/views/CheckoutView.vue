<template>
  <default-layout>
    <div class="title-cont py-[50px]"><span class="title">Checkout</span></div>
    <div class="content-cont">
      <div class="content">
        <router-view></router-view>
        <!-- <div class="separator"></div> -->
        <!-- <div class="checkout-cont">
          <div class="bill-cont">
            <div class="bill-form-cont">
              <div class="sub-title">Billing details</div>
              <div class="bill-form">
                <div class="input-name-cont">
                  <text-field label="First name" :required="true" />
                  <text-field label="Last name" :required="true" />
                </div>
                <text-field label="Company name (optional)" :required="false" />
                <text-field label="Country / Region" :required="true" />
                <text-field
                  label="Street address"
                  :required="true"
                  placeholder="House number and street name"
                />
                <text-field
                  label="Postcode / ZIP (optional)"
                  :required="false"
                />
                <text-field label="Town / City" :required="true" />
                <text-field label="Phone" :required="true" />
                <text-field label="Email address" :required="true" />
              </div>
            </div>
            <div class="note-cont">
              <div class="sub-title">Additional information</div>
              <div class="bill-form">
                <text-field label="Order notes (optional)" :required="false" />
              </div>
            </div>
          </div>
          <div class="order-cont">
            <card-view intent="form" padding="28px 32px">
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
                <radio-field
                  label="Direct bank transfer"
                  name="payment-method"
                />
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
        </div> -->
      </div>
    </div>
  </default-layout>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import DefaultLayout from '../layouts/DefaultLayout.vue';
import TextField from '../components/common/TextField.vue';
import CardView from '../components/common/CardView.vue';
import CustomButton from '../components/common/CustomButton.vue';
import RadioField from '../components/common/RadioField.vue';

export default defineComponent({
  name: 'CheckoutView',
  components: {
    DefaultLayout,
    TextField,
    CardView,
    CustomButton,
    RadioField,
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.title-cont {
  .title {
    margin: auto;
    width: 120rem;
    max-width: 100%;
    display: block;
    padding: 1rem;
    font-size: $--font-8xl;
    font-weight: $--font-bold;
    text-align: center;
  }
}
.content-cont {
  margin: auto;
  width: 120rem;
  max-width: 100%;
  padding-bottom: 8rem;
  .content {
    padding: 1rem;
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
          font-size: $--font-xl;
          font-weight: $--font-bold;
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
  }
}
</style>
