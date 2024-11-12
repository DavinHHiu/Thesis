<template>
  <div class="separator"></div>
  <div class="checkout-cont">
    <div class="bill-cont">
      <div class="address-form-cont">
        <h2 class="sub-title" v-t="'checkoutPage.subtitle.address'" />
        <div v-if="addresses.length > 0">
          <address-select
            :open-add-btn="!openAddressForm"
            @add:address="addAddress"
            @edit:address="editAddress"
          />
        </div>
        <div v-if="addresses.length === 0 || openAddressForm" class="bill-form">
          <div>
            <select-field
              :label="'inputLabel.checkout.city'"
              :options="[
                { displayValue: 'Ha Noi', value: 'Ha Noi' },
                { displayValue: 'Hai Phong', value: 'Hai Phong' },
              ]"
              :value="address?.city"
              @update:model-value="(newValue) => (address.city = newValue)"
            />
          </div>
          <div>
            <select-field
              :label="'inputLabel.checkout.district'"
              :options="[
                { displayValue: 'Ba Dinh', value: 'Ba Dinh' },
                { displayValue: 'Tay Ho', value: 'Tay Ho' },
              ]"
              :value="address?.district"
              @update:model-value="(newValue) => (address.district = newValue)"
            />
          </div>
          <div>
            <select-field
              :label="'inputLabel.checkout.ward'"
              :options="[
                { displayValue: 'Phuc Xa', value: 'Phuc Xa' },
                { displayValue: 'Quan Thanh', value: 'Quan Thanh' },
              ]"
              :value="address?.ward"
              @update:model-value="(newValue) => (address.ward = newValue)"
            />
          </div>
          <div>
            <text-field
              class="h-[4.5rem]"
              :label="'inputLabel.checkout.address1'"
              :required="true"
              :value="address?.address_1"
              @update:model-value="(newValue) => (address.address_1 = newValue)"
            />
          </div>
          <div>
            <text-field
              class="h-[4.5rem]"
              :label="'inputLabel.checkout.address2'"
              :required="true"
              :value="address?.address_2"
              @update:model-value="(newValue) => (address.address_2 = newValue)"
            />
          </div>
        </div>
      </div>
      <div
        v-if="addresses.length === 0 || openAddressForm"
        class="contact-form-cont"
      >
        <h2 class="sub-title" v-t="'checkoutPage.subtitle.contact'" />
        <div class="bill-form">
          <div>
            <text-field
              class="h-[4.5rem]"
              :label="'inputLabel.checkout.phone'"
              :required="true"
              :value="address?.tel"
              @update:model-value="(newValue) => (address.tel = newValue)"
            />
          </div>
          <div>
            <text-field
              class="h-[4.5rem]"
              :label="'inputLabel.checkout.representative'"
              :required="true"
              :value="address?.representative"
              @update:model-value="
                (newValue) => (address.representative = newValue)
              "
            />
          </div>
        </div>
        <div class="flex flex-col">
          <div class="flex w-full gap-[2rem] justify-end">
            <custom-button
              v-if="addresses.length > 0"
              class="btn w-1/2 py-[1.4rem] px-[2.8rem]"
              intent="p-outline"
              v-html="$t('buttonLabel.cancel')"
              @click="cancelAdd"
            />
            <custom-button
              class="btn w-1/2 py-[1.4rem] px-[2.8rem]"
              intent="primary"
              v-html="$t('buttonLabel.save')"
              @click="addNewAddress"
            />
          </div>
          <custom-button
            v-if="editing"
            class="btn w-full py-[1.4rem] px-[2.8rem]"
            intent="danger"
            data-bs-toggle="modal"
            data-bs-target="#deleteModal"
            v-html="$t('buttonLabel.delete')"
          />
        </div>
      </div>
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
              <td class="product-total" v-text="`$${item.subtotal}.00`" />
            </tr>
          </tbody>
          <tfoot>
            <tr>
              <th class="product-name" v-t="'checkoutPage.thead.quantity'" />
              <td class="product-total" v-text="totalQuantity" />
            </tr>
            <tr>
              <th class="product-name" v-t="'checkoutPage.thead.subtotal'" />
              <td class="product-total" v-text="`$${totalAmount}.00`" />
            </tr>
            <tr>
              <th class="product-name" v-t="'checkoutPage.thead.shippingFee'" />
              <td
                class="product-total"
                v-text="`$${shipmentMethod.shipping_fee}.00`"
              />
            </tr>
            <tr>
              <th class="product-name" v-t="'checkoutPage.thead.total'" />
              <td
                class="product-total"
                v-text="`$${totalAmount + shipmentMethod.shipping_fee}.00`"
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
          v-html="$t('checkoutPage.btnLabel.placeOrder')"
          @click="handlePlaceOrder"
        />
      </card>
    </div>
  </div>
  <modal
    id="deleteModal"
    :title="'addressPage.deleteModel.title'"
    @submit="deleteAddress"
  >
    <span v-t="'addressPage.deleteModel.content'" />
  </modal>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import CustomLabel from "@/components/common/atomic/CustomLabel.vue";
import Card from "@/components/common/molecules/Card.vue";
import RadioField from "@/components/common/molecules/RadioField.vue";
import SelectField from "@/components/common/molecules/SelectField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import AddressSelect from "@/components/common/organisms/AddressSelect.vue";
import Modal from "@/components/common/organisms/Modal.vue";
import ShipmentSelect from "@/components/common/organisms/ShipmentSelect.vue";
import { useAddressStore } from "@/stores/address";
import { useCartStore } from "@/stores/cart";
import { usePaymentStore } from "@/stores/payment";
import { useShipmentStore } from "@/stores/shipment";
import { Address, CartItem, isAddressValid, User } from "@/types/worker";
import localStore from "@/utils/localStorage";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "CheckoutFormView",
  components: {
    AddressSelect,
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
      totalQuantity: 0,
      totalAmount: 0,
      paymentMethodCurIdx: 0,
      openAddressForm: false,
      editing: false,
    };
  },
  computed: {
    ...mapState(useCartStore, ["checkoutItems"]),
    ...mapState(useAddressStore, ["address", "addresses"]),
    ...mapState(usePaymentStore, ["paymentMethods"]),
    ...mapState(useShipmentStore, ["shipmentMethod", "shipmentMethods"]),
  },
  methods: {
    ...mapActions(useCartStore, ["createPayment"]),
    ...mapActions(usePaymentStore, ["listPaymentMethods"]),
    ...mapActions(useAddressStore, [
      "createAddress",
      "updateAddress",
      "listAddressesByUser",
      "destroyAddress",
      "setAddress",
    ]),
    ...mapActions(useShipmentStore, ["setShipmentMethod"]),
    async handlePlaceOrder() {
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
    async addNewAddress() {
      if (!this.address.user_id) {
        const user = localStore.get("user") as User;
        if (user && user.id) {
          this.address.user_id = user.id;
        }
      }
      if (isAddressValid(this.address)) {
        if (this.address.id) {
          const response = await this.updateAddress(this.address);
          if (response && response.status === 200) {
            this.openAddressForm = false;
          }
        } else {
          const response = await this.createAddress(this.address);
          if (response && response.status === 201) {
            this.openAddressForm = false;
          }
        }
      } else {
        alert("Please fill all the required fields");
      }
    },
    cancelAdd() {
      this.openAddressForm = false;
      this.editing = false;
      this.setAddress({} as Address);
    },
    addAddress() {
      this.setAddress({} as Address);
      this.openAddressForm = true;
    },
    editAddress(id: number) {
      const address = this.addresses.find((addr) => addr.id === id) as Address;
      this.setAddress(address);
      this.editing = true;
      this.openAddressForm = true;
    },
    async deleteAddress() {
      this.destroyAddress(this.address);
      this.setAddress({} as Address);
      this.openAddressForm = false;
      this.editing = false;
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
    await this.listAddressesByUser();
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
      .input-name-cont {
        width: 100%;
        display: flex;
        gap: 4.5rem;
      }
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
