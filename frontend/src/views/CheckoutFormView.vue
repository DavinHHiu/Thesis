<template>
  <div class="separator"></div>
  <div class="checkout-cont">
    <div class="bill-cont">
      <address-form />
      <div class="shipments-cont">
        <h2 class="sub-title" v-t="'checkoutPage.subtitle.shipment'" />
        <div class="bill-form">
          <shipment-select @update:shipment-method="changeShipmentMethod" />
        </div>
      </div>
      <div class="note-cont">
        <h2 class="sub-title" v-t="'checkoutPage.subtitle.additionalInfo'" />
        <div class="bill-form">
          <div>
            <text-field
              class="h-[4.5rem]"
              :label="'inputLabel.checkout.notes'"
              :required="false"
            />
          </div>
        </div>
      </div>
    </div>
    <div class="order-cont">
      <card intent="form" class="form">
        <div class="order-title" v-t="'checkoutPage.subtitle.yourOrder'" />
        <table class="total-cont">
          <thead>
            <tr>
              <th class="product-name" v-t="'checkoutPage.thead.product'" />
              <th class="product-total" v-t="'checkoutPage.thead.amount'" />
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in checkoutItems">
              <td
                class="product-name"
                v-text="`${item?.product?.name} x ${item.quantity}`"
              />
              <td class="product-total" v-text="formatAmount(item.subtotal)" />
            </tr>
          </tbody>
          <tfoot>
            <tr>
              <th class="product-name" v-t="'checkoutPage.thead.quantity'" />
              <td class="product-total" v-text="totalQuantity" />
            </tr>
            <tr>
              <th class="product-name" v-t="'checkoutPage.thead.subtotal'" />
              <td class="product-total" v-text="formatAmount(totalAmount)" />
            </tr>
            <tr>
              <th class="product-name" v-t="'checkoutPage.thead.shippingFee'" />
              <td
                class="product-total"
                v-text="formatAmount(shipmentMethod.shipping_fee)"
              />
            </tr>
            <tr>
              <th class="product-name" v-t="'checkoutPage.thead.total'" />
              <td
                class="product-total"
                v-text="formatAmount(totalAmount + shipmentMethod.shipping_fee)"
              />
            </tr>
          </tfoot>
        </table>
        <div class="payment-method-cont">
          <div
            v-for="(paymentMethod, index) in paymentMethods"
            class="payment-input-cont"
          >
            <radio-field
              :label="paymentMethod.name"
              name="payment-method"
              :check="index === paymentMethodCurIdx"
              @update:input="changePaymentMethod(index)"
            />
            <img
              v-if="paymentMethod.value === 'paypal'"
              src="https://www.paypalobjects.com/webstatic/mktg/logo/AM_mc_vs_dc_ae.jpg"
              alt="PayPal acceptance mark"
            />
          </div>
        </div>
        <custom-button
          intent="primary"
          class="btn w-full py-[16px] px-[28px]"
          :disabled="loading"
          v-html="$t('checkoutPage.btnLabel.placeOrder')"
          @click="handlePlaceOrder"
        />
      </card>
    </div>
  </div>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import CustomLabel from "@/components/common/atomic/CustomLabel.vue";
import Card from "@/components/common/molecules/Card.vue";
import RadioField from "@/components/common/molecules/RadioField.vue";
import SelectField from "@/components/common/molecules/SelectField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import AddressForm from "@/components/common/organisms/AddressForm.vue";
import Modal from "@/components/common/organisms/Modal.vue";
import ShipmentSelect from "@/components/common/organisms/ShipmentSelect.vue";
import { useAddressStore } from "@/stores/address";
import { useCartStore } from "@/stores/cart";
import { usePaymentStore } from "@/stores/payment";
import { useShipmentStore } from "@/stores/shipment";
import { CartItem } from "@/types/worker";
import { formatCurrency } from "@/utils/currency";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";
import { useI18n } from "vue-i18n";

export default defineComponent({
  name: "CheckoutFormView",
  components: {
    AddressForm,
    Card,
    CustomButton,
    CustomLabel,
    RadioField,
    Modal,
    SelectField,
    TextField,
    ShipmentSelect,
  },
  data() {
    return {
      loading: false,
      totalQuantity: 0,
      totalAmount: 0,
      paymentMethodCurIdx: 0,
    };
  },
  computed: {
    ...mapState(useAddressStore, ["address"]),
    ...mapState(useCartStore, ["checkoutItems"]),
    ...mapState(usePaymentStore, ["paymentMethods"]),
    ...mapState(useShipmentStore, ["shipmentMethod", "shipmentMethods"]),
  },
  methods: {
    ...mapActions(useCartStore, ["createPayment"]),
    ...mapActions(usePaymentStore, ["listPaymentMethods"]),
    ...mapActions(useShipmentStore, ["setShipmentMethod"]),
    formatCurrency,
    formatAmount(amount: number) {
      const { locale } = useI18n();
      return this.formatCurrency(locale.value, amount);
    },
    async handlePlaceOrder() {
      this.loading = true;
      const response = await this.createPayment(
        this.totalAmount + this.shipmentMethod.shipping_fee,
        this.totalQuantity,
        this.address,
        this.shipmentMethod,
        this.paymentMethods[this.paymentMethodCurIdx]
      );
      if (!response.data.approval_url) {
        this.$router.push({
          name: "checkout-received",
          params: {
            orderId: response.data.order_id,
          },
        });
      }
    },
    changePaymentMethod(index: number) {
      this.paymentMethodCurIdx = index;
    },
    changeShipmentMethod(index: number) {
      this.setShipmentMethod(this.shipmentMethods[index]);
    },
  },
  watch: {
    checkoutItems: {
      immediate: true,
      handler(newItems) {
        if (newItems.length === 0) {
          this.$router.push({ name: "cartPage" });
        }
        this.totalQuantity = newItems.reduce(
          (acc: number, cur: CartItem) => acc + cur.quantity,
          0
        );
        this.totalAmount = newItems.reduce(
          (acc: number, cur: CartItem) => acc + cur.subtotal,
          0
        );
      },
    },
  },
  async mounted() {
    await this.listPaymentMethods();
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

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
      margin-top: 4rem;
      display: flex;
      flex-direction: column;
      gap: 4rem;
      width: 100%;
    }
  }
  .order-cont {
    width: 40%;
    .form {
      padding: 2rem;
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
  .btn {
    margin-top: 3rem;
    text-transform: uppercase;
  }
}
</style>
