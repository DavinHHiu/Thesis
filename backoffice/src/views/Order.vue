<template>
  <page-title :title="$t('orderPage.list.title')" />
  <page-body>
    <header-action :current-route="$t('orderPage.add.name')" />
    <table class="w-full mt-[2rem] overflow-hidden">
      <thead>
        <tr>
          <th>No.</th>
          <th>User</th>
          <th>Total amount</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="(order, index) in orders" :key="index">
          <tr :class="{ odd: index % 2 == 0 }">
            <td>{{ index + 1 }}</td>
            <td>
              <div class="flex justify-center">
                <img
                  :src="order.user.avatar as string"
                  :alt="order.user.email"
                  class="w-[4rem] h-[4rem] rounded-full object-cover"
                />
              </div>
            </td>
            <td v-text="order.total_amount" />
            <td v-text="order.status" />
            <td class="action-wrap">
              <ellipsis-dropdown
                @action="handleActions"
                :current-index="index"
                :dropdown-list="[
                  { title: 'Detail', action: '' },
                  { title: 'Delete', action: '#deleteModal' },
                ]"
              />
            </td>
          </tr>
        </template>
      </tbody>
    </table>
  </page-body>
  <modal id="deleteModal" title="Delete attribute" @confirm="submitAction">
    <span v-text="$t('orderPage.modalDelete.title')" />
  </modal>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import EllipsisDropdown from "@/components/common/molecules/EllipsisDropdown.vue";
import HeaderAction from "@/components/common/molecules/HeaderAction.vue";
import Modal from "@/components/common/molecules/Modal.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useOrderStore } from "@/stores/order";
import { Order } from "@/types/worker";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "OrderView",
  components: {
    CustomButton,
    EllipsisDropdown,
    HeaderAction,
    Modal,
    PageTitle,
    PageBody,
  },
  data() {
    return {
      currentAction: "" as string,
      currentIndex: 0 as number,
    };
  },
  methods: {
    ...mapActions(useOrderStore, ["listOrders", "destroyOrder"]),
    handleActions(obj: any) {
      const order = this.orders[obj.currentIndex];
      if (obj.action === "Detail") {
        this.$router.push({
          name: "order.update",
          params: { orderId: order.id },
        });
      }
      this.currentAction = obj.action;
      this.currentIndex = obj.currentIndex;
    },
    async submitAction() {
      const action = this.currentAction;
      if (action === "Delete") {
        const order = this.orders[this.currentIndex] as Order;
        if (order.id) {
          this.destroyOrder(order.id);
        }
      }
    },
  },
  computed: {
    ...mapState(useOrderStore, ["orders"]),
  },
  async mounted() {
    await this.listOrders();
  },
});
</script>
