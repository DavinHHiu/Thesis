<template>
  <page-title :title="$t('cartPage.list.title')" />
  <page-body>
    <header-action :current-route="$t('cartPage.add.name')" />
    <table class="w-full mt-[2rem] overflow-hidden">
      <thead>
        <tr>
          <th>No.</th>
          <th>Total quantity</th>
          <th>Total amount</th>
          <th>User</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="(cart, index) in carts" :key="index">
          <tr :class="{ odd: index % 2 == 0 }">
            <td>{{ index + 1 }}</td>
            <td v-text="cart.total_quantity" />
            <td v-text="cart.total_amount" />
            <td>
              <div class="flex justify-center">
                <img
                  :src="cart.user.avatar as string"
                  :alt="cart.user.email"
                  class="w-[4rem] h-[4rem] rounded-full object-cover"
                />
              </div>
            </td>
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
import { useCartStore } from "@/stores/cart";
import { Cart } from "@/types/worker";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "AddressView",
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
    ...mapActions(useCartStore, ["listCarts", "destroyCart"]),
    handleActions(obj: any) {
      const cart = this.carts[obj.currentIndex];
      if (obj.action === "Detail") {
        this.$router.push({
          name: "cart.update",
          params: { cartId: cart.id },
        });
      }
      this.currentAction = obj.action;
      this.currentIndex = obj.currentIndex;
    },
    async submitAction() {
      const action = this.currentAction;
      if (action === "Delete") {
        const cart = this.carts[this.currentIndex] as Cart;
        if (cart.id) {
          this.destroyCart(cart.id);
        }
      }
    },
  },
  computed: {
    ...mapState(useCartStore, ["carts"]),
  },
  async mounted() {
    await this.listCarts();
  },
});
</script>
