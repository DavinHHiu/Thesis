<template>
  <default-layout>
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
  </default-layout>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import DefaultLayout from '../layouts/DefaultLayout.vue';
import PageTitle from '../components/common/PageTitle.vue';
import PageBody from '../components/common/PageBody.vue';
import SeparatorLine from '../components/common/SeparatorLine.vue';
import NavPills from '../components/common/NavPills.vue';
import PagingNumber from '../components/common/PagingNumber.vue';
import { returnPaginationRange } from '../utils/utils';

export default defineComponent({
  name: 'OrderView',
  components: {
    DefaultLayout,
    PageTitle,
    PageBody,
    SeparatorLine,
    NavPills,
    PagingNumber,
  },
  data() {
    return {
      items: [
        { title: 'All', quantity: 3 },
        { title: 'Processing', quantity: 2 },
        { title: 'Shipping', quantity: 1 },
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
.list-orders-wp {
  margin-top: 20px;
  width: 100%;
  border: 1px solid #e2e2e2;
  font-size: 16px;
  tbody tr {
    border-top: 1px solid #e2e2e2;
  }
  th,
  td {
    padding: 12px 16px;
    font-weight: 500;
  }
  th {
    text-align: left;
    font-weight: 600;
    background-color: #fff;
  }
  .item-image {
    width: 110px;
    height: 100px;
  }
  .item-total-amount {
    font-weight: 600;
  }
  .item-list-product {
    text-align: center;
  }
}
</style>
