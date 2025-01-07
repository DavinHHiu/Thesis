<template>
  <page-title title="orderPage.title" />
  <page-body>
    <LoadingPage v-if="loadingPage" />
    <separator-line class="mb-[3.2rem]" />
    <nav-pills :items="items" @update:change-status="changeStatus" />
    <table class="list-orders-wp">
      <thead>
        <tr>
          <th v-t="'orderPage.thead.orderNumber'" />
          <th v-t="'orderPage.thead.shippingDate'" />
          <th v-t="'orderPage.thead.paymentMethod'" />
          <th v-t="'orderPage.thead.totalQuantity'" />
          <th v-t="'orderPage.thead.total'" />
          <th v-t="'orderPage.thead.status'" />
          <th />
        </tr>
      </thead>
      <tbody>
        <template v-for="order in orders" :key="order?.id">
          <tr class="item-cont">
            <td class="item-id" v-text="order?.id" />
            <td class="item-shipment">
              <span
                class="item-shipment-method"
                v-text="order?.shipment?.shipment_method?.name"
              />
              <span
                class="item-shipment-date"
                v-text="formatDate(order?.shipment?.shipping_date)"
              />
            </td>
            <td
              class="item-payment"
              v-text="order?.payment?.payment_method?.name"
            />
            <td class="item-quantity" v-text="order?.total_quantity" />
            <td
              class="item-total-amount"
              v-text="formatAmount(order?.payment?.total_amount)"
            />
            <td><status-pill :status="order?.status as StatusType" /></td>
            <td
              class="item-detail"
              v-t="'orderPage.label.detail'"
              @click="goToDetail(order?.id as string)"
            />
          </tr>
        </template>
      </tbody>
    </table>
    <paging-number
      class="pagination"
      :paging="paging"
      :cur-page="currentPage"
      @change-page="changePage"
    />
  </page-body>
</template>

<script lang="ts">
import StatusPill from "@/components/common/atomic/StatusPill.vue";
import NavPills from "@/components/common/molecules/NavPills.vue";
import PagingNumber from "@/components/common/molecules/PagingNumber.vue";
import SeparatorLine from "@/components/common/molecules/SeparatorLine.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import consts, { StatusType } from "@/consts/consts";
import { useOrderStore } from "@/stores/order";
import { NavPillItem as iNavPill } from "@/types/common";
import { formatCurrency } from "@/utils/currency";
import { formatDate } from "@/utils/date";
import { getPaginationRange } from "@/utils/utils";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";
import { useI18n } from "vue-i18n";

export default defineComponent({
  name: "OrderView",
  components: {
    PageTitle,
    PageBody,
    SeparatorLine,
    StatusPill,
    NavPills,
    PagingNumber,
  },
  data() {
    return {
      items: [] as iNavPill[],
      array: [],
      counter: {},
      resultsCount: 0,
      limit: 50,
      offset: 0,
      currentPage: 1,
      loadingPage: false,
      currentStatus: "all",
    };
  },
  computed: {
    ...mapState(useOrderStore, ["orders"]),
    paging() {
      return getPaginationRange(
        Math.floor(this.resultsCount / this.limit) + 1,
        this.currentPage,
        1
      );
    },
  },
  methods: {
    ...mapActions(useOrderStore, ["listOrders"]),
    changeStatus(item: iNavPill) {
      this.offset = 0;
      const params = {
        limit: this.limit,
        offset: this.offset,
        status: item.title !== consts.ALL_STATUS ? item.title : undefined,
      };
      this.listOrders(params);
      this.currentStatus = item.title;
    },
    formatAmount(amount: number) {
      const { locale } = useI18n();
      return formatCurrency(locale.value, amount);
    },
    goToDetail(orderId: string) {
      this.$router.push({
        name: "checkout-received",
        params: {
          orderId,
        },
      });
    },
    async changePage(page: number) {
      this.currentPage = page;
      this.offset = (page - 1) * this.limit;
      this.loadingPage = true;
      const params = {
        limit: this.limit,
        offset: this.offset,
        status: this.currentStatus,
      };
      await this.listOrders(params);
      this.loadingPage = false;
    },
    formatDate,
  },
  watch: {
    counter: {
      handler() {
        const total = Object.values(
          this.counter as { [key: string]: number }
        ).reduce((sum, value) => sum + value, 0);
        const result = Object.entries(this.counter).map(([key, value]) => ({
          title: key,
          quantity: value as number,
        }));
        this.items = [{ title: consts.ALL_STATUS, quantity: total }, ...result];
      },
      immediate: true,
    },
  },
  async mounted() {
    const params = {
      limit: this.limit,
      offset: this.offset,
    };
    const response = await this.listOrders(params);
    this.counter = response.data.counter;
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
  }
  th {
    text-align: left;
    font-weight: $--font-bold;
    background-color: $--second-color;
  }
  .item-id {
    width: 40rem;
  }
  .item-total-amount {
    font-weight: $--font-bold;
  }
  .item-shipment {
    display: flex;
    flex-direction: column;
  }
  .item-list-product {
    text-align: center;
  }
  .item-shipment-method {
    color: $--title-color-text;
  }
  .item-shipment-date {
    font-size: $--font-2xs;
    font-weight: $--font-bold;
  }
  .item-detail {
    color: $--color-blue;
    font-size: $--font-xs;
    &:hover {
      text-decoration: underline;
      cursor: pointer;
    }
  }
}
</style>
