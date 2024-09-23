<template>
  <page-body>
    <header-action :current-route="$t('orderItemPage.add.name')" />
    <table class="w-full mt-[2rem] overflow-hidden">
      <thead>
        <tr>
          <th>No.</th>
          <th />
          <th>Product</th>
          <th>Price</th>
          <th>Quantity</th>
          <th>Subtotal</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="(orderItem, index) in orderItems" :key="index">
          <tr :class="{ odd: index % 2 == 0 }">
            <td>{{ index + 1 }}</td>
            <td>
              <div class="flex justify-center">
                <img
                  :src="orderItem.product_sku.images?.[0].image"
                  alt=""
                  class="w-[4rem] h-[5rem] object-cover"
                />
              </div>
            </td>
            <td v-text="orderItem.product_sku?.product.name" />
            <td v-text="orderItem.product_sku.price" />
            <td v-text="orderItem.quantity" />
            <td v-text="orderItem.subtotal" />
            <td class="action-wrap">
              <ellipsis-dropdown
                @action="handleActions"
                :current-index="index"
                :dropdown-list="[
                  { title: 'Update', action: '' },
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
    <span v-text="$t('addressPage.modalDelete.title')" />
  </modal>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import EllipsisDropdown from "@/components/common/molecules/EllipsisDropdown.vue";
import HeaderAction from "@/components/common/molecules/HeaderAction.vue";
import Modal from "@/components/common/molecules/Modal.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useOrderItemStore } from "@/stores/orderItem";
import { OrderItem } from "@/types/worker";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "OrderItemView",
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
    ...mapActions(useOrderItemStore, ["listOrderItems", "destroyOrderItem"]),
    handleActions(obj: any) {
      const orderItem = this.orderItems[obj.currentIndex];
      if (obj.action === "Update") {
        this.$router.push({
          name: "order.item.update",
          params: { orderItemId: orderItem.id },
        });
      }
      this.currentAction = obj.action;
      this.currentIndex = obj.currentIndex;
    },
    async submitAction() {
      const action = this.currentAction;
      if (action === "Delete") {
        const orderItem = this.orderItems[this.currentIndex] as OrderItem;
        if (orderItem.id) {
          this.destroyOrderItem(orderItem.id);
        }
      }
    },
  },
  computed: {
    ...mapState(useOrderItemStore, ["orderItems"]),
  },
  async mounted() {
    await this.listOrderItems();
  },
});
</script>
