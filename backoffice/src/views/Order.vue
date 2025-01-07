<template>
  <page-title title="orderPage.title" />
  <page-body>
    <nav-pills :items="items" @update:change-status="changeStatus" />
    <table class="w-full mt-[2rem] overflow-hidden">
      <thead>
        <tr>
          <th v-t="'orderPage.thead.orderNumber'" />
          <th v-t="'orderPage.thead.shipment'" />
          <th v-t="'orderPage.thead.paymentMethod'" />
          <th v-t="'orderPage.thead.totalQuantity'" />
          <th v-t="'orderPage.thead.total'" />
          <th v-t="'orderPage.thead.status'" />
          <th />
          <th />
        </tr>
      </thead>
      <tbody>
        <template v-for="(order, index) in orders" :key="order?.id">
          <tr class="item-cont" :class="{ odd: !(index % 2) }">
            <td class="item-id" v-text="fmt(order.id)" />
            <td>
              <div class="item-shipment">
                <span
                  class="item-shipment-method"
                  v-text="fmt(order?.shipment?.shipment_method?.name)"
                />
                <span
                  class="item-shipment-date"
                  v-text="fmtDate(order?.shipment?.shipping_date)"
                />
              </div>
            </td>
            <td
              class="item-payment"
              v-text="fmt(order?.payment?.payment_method?.name)"
            />
            <td class="item-quantity" v-text="fmt(order?.total_quantity)" />
            <td
              class="item-total-amount"
              v-text="fmtAmount(order?.payment?.total_amount)"
            />
            <td>
              <div class="flex justify-center">
                <status-pill :status="order?.status as StatusType" />
              </div>
            </td>
            <td
              class="item-detail"
              v-t="'orderPage.label.detail'"
              @click="goToDetail(order?.id as string)"
            />
            <td class="action-wrap">
              <ellipsis-dropdown
                v-if="createDropdownList(order)"
                @action="handleActions"
                :current-index="index"
                :dropdown-list="createDropdownList(order) || []"
              />
            </td>
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
    <!-- <paging-number class="pagination" :paging="array" /> -->
  </page-body>
</template>

<script lang="ts">
import StatusPill from "@/components/common/atomic/StatusPill.vue";
import EllipsisDropdown from "@/components/common/molecules/EllipsisDropdown.vue";
import NavPills from "@/components/common/molecules/NavPills.vue";
import PagingNumber from "@/components/common/molecules/PagingNumber.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import consts, { StatusType } from "@/consts/consts";
import { useOrderStore } from "@/stores/order";
import { DropdownItem, NavPillItem as iNavPill } from "@/types/backoffice";
import { Order } from "@/types/worker";
import { fmt, fmtCur, fmtDate } from "@/utils/utils";
import { getPaginationRange } from "@/utils/utils";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";
import { useI18n } from "vue-i18n";

export default defineComponent({
  name: "OrderView",
  components: {
    EllipsisDropdown,
    PageTitle,
    PageBody,
    NavPills,
    StatusPill,
    PagingNumber,
  },
  data() {
    return {
      items: [] as iNavPill[],
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
    ...mapActions(useOrderStore, ["listOrders", "updateOrderStatus"]),
    fmtAmount(amount: number) {
      const { locale } = useI18n();
      return fmtCur(locale.value, amount);
    },
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
    goToDetail(orderId: string) {
      this.$router.push({
        name: "checkout-received",
        params: {
          orderId,
        },
      });
    },
    createDropdownList(order: Order) {
      const idx = consts.ORDER_STATUSES.indexOf(order.status);
      const nextStatus = consts.ORDER_STATUSES[idx + 1];
      const dropdownList = [] as DropdownItem[];

      if (consts.CHANGABLE_ORDER_STATUSES.includes(order.status)) {
        dropdownList.push({
          title: `Change to ${nextStatus}`,
          action: nextStatus,
        });
      }

      if (order.status === consts.ORDER_STATUS_PENDING) {
        dropdownList.push({
          title: this.$t("orderPage.label.cancel"),
          action: consts.ORDER_STATUS_CANCELLED,
        });
      }

      return dropdownList.length > 0 ? dropdownList : undefined;
    },
    handleActions(obj: any) {
      const order = this.orders[obj.currentIndex];
      if (order && order.id) {
        this.updateOrderStatus(order.id, obj.action);
      }
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
    fmtDate,
    fmt,
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
@import "@/assets/scss/variables";

.item-detail {
  color: $--color-blue;
  font-size: $--font-xs;
  &:hover {
    text-decoration: underline;
    cursor: pointer;
  }
}

.item-total-amount {
  font-weight: $--font-bold;
}

.item-shipment {
  display: flex;
  flex-direction: column;
  .item-shipment-method {
    color: $--dark-gray;
  }
  .item-shipment-date {
    font-size: $--font-2xs;
    font-weight: $--font-bold;
  }
}
</style>
