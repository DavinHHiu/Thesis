<template>
  <page-title title="Orders" />
  <page-body>
    <separator-line class="mb-[32px]" />
    <nav-pills :items="items" />
    <table class="list-orders-wp">
      <thead>
        <tr>
          <th>Order ID</th>
          <th>Image</th>
          <th>Shipping method</th>
          <th>Shipping date</th>
          <th>Status</th>
          <th>Payment method</th>
          <th>Total amount</th>
          <th>List products</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="(item, index) in 3" :key="index">
          <tr class="item-cont">
            <td class="item-id">OR6789</td>
            <td class="item-image">
              <img
                class="h-full w-full"
                src="https://websitedemos.net/brandstore-02/wp-content/uploads/sites/150/2021/03/sports-shoe3-300x300.jpg"
              />
            </td>
            <td class="item-shipping-method">Express</td>
            <td class="item-delivery">Tue 01/01/2025</td>
            <td class="item-status">Shipping</td>
            <td class="item-payment-method">COD</td>
            <td class="item-total-amount">$150.00</td>
            <td class="item-list-product">Show</td>
          </tr>
        </template>
      </tbody>
    </table>
    <paging-number class="pagination" :paging="array" />
  </page-body>
</template>

<script lang="ts">
import { defineComponent } from "vue";

import NavPills from "../components/common/molecules/NavPills.vue";
import PagingNumber from "../components/common/molecules/PagingNumber.vue";
import SeparatorLine from "../components/common/molecules/SeparatorLine.vue";
import PageBody from "../components/common/templates/PageBody.vue";
import PageTitle from "../components/common/templates/PageTitle.vue";
import { returnPaginationRange } from "../utils/utils";

export default defineComponent({
  name: "OrderView",
  components: {
    PageTitle,
    PageBody,
    SeparatorLine,
    NavPills,
    PagingNumber,
  },
  data() {
    return {
      items: [
        { title: "All", quantity: 3 },
        { title: "Processing", quantity: 2 },
        { title: "Shipping", quantity: 1 },
      ],
      array: [],
    };
  },
  mounted() {
    this.array = returnPaginationRange(15, 1, 5, 1);
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.list-orders-wp {
  margin-top: 2rem;
  width: 100%;
  border: 1px solid $--color-border;
  font-size: $--font-base;
  tbody tr {
    border-top: 1px solid $--color-border;
  }
  th,
  td {
    padding: 1.2rem 1.6rem;
    font-weight: $--font-semibold;
  }
  th {
    text-align: left;
    font-weight: $--font-bold;
    background-color: $--second-color;
  }
  .item-image {
    width: 11rem;
    height: 10rem;
  }
  .item-total-amount {
    font-weight: $--font-base;
  }
  .item-list-product {
    text-align: center;
  }
}
</style>
