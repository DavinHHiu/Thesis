<template>
  <div class="wrapper">
    <p v-t="'receivedOrderPage.message.thank'" />
    <ul class="order-info">
      <li class="order-info-item">
        <span class="uppercase" v-t="'receivedOrderPage.label.orderNumber'" />
        <strong v-text="order?.id" />
      </li>
      <li class="order-info-item">
        <span
          class="uppercase"
          v-t="'receivedOrderPage.label.estimateShippingDate'"
        />
        <strong v-text="order?.shipment?.shipping_date" />
      </li>
      <li class="order-info-item">
        <span class="uppercase" v-t="'receivedOrderPage.label.total'" />
        <strong v-text="formattedAmount(order?.payment?.total_amount)" />
      </li>
      <li class="order-info-item">
        <span class="uppercase" v-t="'receivedOrderPage.label.paymentMethod'" />
        <strong v-text="order?.payment?.payment_method?.name" />
      </li>
    </ul>
    <section class="order-detail">
      <h2
        class="section-title"
        v-t="'receivedOrderPage.subtitle.orderDetails'"
      />
      <table class="order-detail-content">
        <thead>
          <tr>
            <th v-t="'receivedOrderPage.label.product'" />
            <th v-t="'receivedOrderPage.label.total'" />
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in orderItems">
            <td v-text="`${item?.product?.name} x ${item.quantity}`" />
            <td v-text="formattedAmount(item?.product_sku?.price)" />
          </tr>
        </tbody>
        <tfoot>
          <tr>
            <td v-t="'receivedOrderPage.label.totalQuantity'" />
            <td v-text="order?.total_quantity" />
          </tr>
          <tr>
            <td v-t="'receivedOrderPage.label.shippingFee'" />
            <td
              v-text="
                formattedAmount(order?.shipment?.shipment_method?.shipping_fee)
              "
            />
          </tr>
          <tr>
            <td v-t="'receivedOrderPage.label.total'" />
            <td v-text="formattedAmount(order?.payment?.total_amount)" />
          </tr>
          <tr>
            <td v-t="'receivedOrderPage.label.paymentMethod'" />
            <td v-text="order?.payment?.payment_method?.name" />
          </tr>
        </tfoot>
      </table>
    </section>
    <section class="billing-address">
      <h2
        class="section-title"
        v-t="'receivedOrderPage.subtitle.billingAddress'"
      />
      <div class="custom-info-wp">
        <p v-text="order?.shipment?.receive_address?.representative" />
        <p v-text="order?.shipment?.receive_address?.address_1" />
        <p v-text="order?.shipment?.receive_address?.display_address1" />
        <p><span>&#9742; </span>{{ order?.shipment?.receive_address?.tel }}</p>
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import { useOrderStore } from "@/stores/order";
import { formatCurrency } from "@/utils/currency";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";
import { useI18n } from "vue-i18n";

export default defineComponent({
  name: "CheckoutOrderView",
  components: {},
  computed: {
    ...mapState(useOrderStore, ["order", "orderItems"]),
    address() {
      return (
        this.order?.shipment?.receive_address?.ward +
        ", " +
        this.order?.shipment?.receive_address?.district +
        ", " +
        this.order?.shipment?.receive_address?.city
      );
    },
  },
  methods: {
    ...mapActions(useOrderStore, ["retrieveOrder", "listOrderItems"]),
    formattedAmount(amount: number) {
      const { locale } = useI18n();
      return formatCurrency(locale.value, amount);
    },
    formatCurrency,
  },
  async mounted() {
    const orderId = this.$route.params.orderId;
    await this.retrieveOrder(orderId as string);
    await this.listOrderItems(orderId as string);
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.wrapper {
  display: flex;
  flex-direction: column;
  gap: 3.5rem;
  .order-info {
    display: flex;
    .order-info-item {
      font-size: $--font-xs;
      display: flex;
      flex-direction: column;
      padding-right: 2.3rem;
      margin-right: 2.3rem;
      strong {
        font-size: $--font-base;
      }
      &:not(:last-child) {
        border-right: 1px dashed $--color-border;
      }
    }
  }
  .section-title {
    width: 100%;
    padding: 2.1rem;
    border: 1px solid $--color-border;
  }
  .order-detail-content {
    margin-top: -0.1rem;
    font-size: $--font-base;
    width: 100%;
    thead tr {
      border: 1px solid $--color-border;
    }
    th,
    td {
      padding: 1.1rem 1.6rem;
      line-height: 2;
    }
    td {
      border: 1px solid $--color-border;
    }
    th {
      text-align: left;
      font-weight: $--font-bold;
    }
  }
  .custom-info-wp {
    display: flex;
    flex-direction: column;
    margin-top: -0.1rem;
    font-size: $--font-base;
    padding: 1.6rem;
    border: 1px solid $--color-border;
    gap: 0.5rem;
  }
}
</style>
