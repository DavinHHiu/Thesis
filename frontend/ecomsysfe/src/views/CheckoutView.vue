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

<style scoped>
.title-cont {
  .title {
    margin: auto;
    max-width: 1200px;
    display: block;
    padding: 10px;
    font-size: 60px;
    font-weight: 600;
    text-align: center;
  }
}
.content-cont {
  margin: auto;
  max-width: 1200px;
  padding-bottom: 80px;
  .content {
    padding: 10px;
    .separator {
      width: 100%;
      border-top: 3px solid #333;
      margin-bottom: 32px;
    }
    .checkout-cont {
      display: flex;
      justify-content: space-between;

      .bill-cont {
        width: 55%;
        margin-bottom: 30px;
        .sub-title {
          font-size: 20px;
          font-weight: 600;
          padding: 20px 0 14px;
          margin-bottom: 20px;
          border-bottom: 1px solid #e2e2e2;
        }
        .bill-form {
          display: flex;
          flex-direction: column;
          gap: 20px;
          width: 100%;
          .input-name-cont {
            width: 100%;
            display: flex;
            gap: 45px;
          }
        }
      }
      .order-cont {
        width: 40%;
        .order-title {
          font-size: 18px;
          font-weight: 600;
          padding-bottom: 20px;
        }
        .total-cont {
          width: 100%;
          font-size: 15px;
          thead tr th {
            font-weight: 600;
          }
          tr {
            border-bottom: 1px solid #e2e2e2;
          }
          th {
            padding: 14px 12px 14px 0;
          }
          td {
            padding: 10px 10px 10px 0;
          }
          .product-name {
            text-align: left;
          }
          .product-total {
            text-align: right;
          }
        }
        .payment-method-cont {
          color: #000;
          margin-top: 40px;
          display: flex;
          flex-direction: column;
          font-size: 15px;
          gap: 15px;
          margin-bottom: 25px;
          .payment-input-cont {
            display: flex;
            align-items: center;
            gap: 20px;
            img {
              height: 50px;
              width: auto;
            }
          }
        }
      }
    }
  }
}
</style>
