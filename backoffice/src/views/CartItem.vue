<template>
  <page-body>
    <header-action :current-route="$t('cartItemPage.add.name')" />
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
        <template v-for="(cartItem, index) in cartItems" :key="index">
          <tr :class="{ odd: index % 2 == 0 }">
            <td>{{ index + 1 }}</td>
            <td>
              <div class="flex justify-center">
                <img
                  :src="cartItem.product_sku.images?.[0].image"
                  alt=""
                  class="w-[4rem] h-[5rem] object-cover"
                />
              </div>
            </td>
            <td v-text="cartItem.product_sku?.product.name" />
            <td v-text="cartItem.product_sku.price" />
            <td v-text="cartItem.quantity" />
            <td v-text="cartItem.subtotal" />
            <td class="action-wrap">
              <ellipsis-dropdown
                @action="handleActions"
                :current-index="index"
                :dropdown-list="[
                  { title: 'Update', action: 'update' },
                  { title: 'Delete', action: 'openModal' },
                ]"
              />
            </td>
          </tr>
        </template>
      </tbody>
    </table>
  </page-body>
  <modal
    ref="deleteModal"
    id="deleteModal"
    title="Delete attribute"
    @confirm="handleDelete"
  >
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
import { useCartItemStore } from "@/stores/cartItem";
import { CartItem } from "@/types/worker";
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
      currentIndex: 0 as number,
    };
  },
  methods: {
    ...mapActions(useCartItemStore, ["listCartItems", "destroyCartItem"]),
    handleActions(obj: any) {
      const cartItem = this.cartItems[obj.currentIndex];
      if (obj.action === "update") {
        this.$router.push({
          name: "cart.item.update",
          params: { cartItemId: cartItem.id },
        });
      } else if (obj.action === "openModal") {
        const modal = this.$refs.deleteModal as InstanceType<typeof Modal>;
        modal.open();
      }
      this.currentIndex = obj.currentIndex;
    },
    async handleDelete() {
      const cartItem = this.cartItems[this.currentIndex] as CartItem;
      if (cartItem.id) {
        this.destroyCartItem(cartItem.id);
      }
    },
  },
  computed: {
    ...mapState(useCartItemStore, ["cartItems"]),
  },
  async mounted() {
    await this.listCartItems();
  },
});
</script>
