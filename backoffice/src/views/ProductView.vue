<template>
  <page-title title="Products" />
  <page-body>
    <div class="action-wrap flex justify-between">
      <custom-button intent="p-outline">
        <span class="material-symbols-outlined">filter_alt</span>
        Filter
      </custom-button>
      <custom-button :rounded="true">
        <span class="material-symbols-outlined">add</span>
        Add
      </custom-button>
    </div>

    <table class="w-full mt-[2rem] overflow-hidden">
      <thead>
        <tr>
          <th>No.</th>
          <th>Cover</th>
          <th>Name</th>
          <th>Sku</th>
          <th>Size</th>
          <th>Color</th>
          <th>Category</th>
          <th>Quantity</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="(product, index) in products" :key="index">
          <tr :class="{ odd: index % 2 == 0 }">
            <td>{{ index + 1 }}</td>
            <td>
              <div class="flex justify-center">
                <img
                  :src="product.cover as string"
                  :alt="product.name"
                  class="w-[5rem] h-[7rem] object-cover"
                />
              </div>
            </td>
            <td v-text="product.name" />
            <td v-text="product.sku" />
            <td v-text="product.size.value" />
            <td v-text="product.color.value" />
            <td v-text="product.categories[0].name" />
            <td v-text="product.quantity" />
            <td v-text="product.price" />
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
    <span>Do you want to delete this user?</span>
  </modal>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import EllipsisDropdown from "@/components/common/molecules/EllipsisDropdown.vue";
import Modal from "@/components/common/molecules/Modal.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useProductStore } from "@/stores/product";
import { Product } from "@/types/worker";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "ProductView",
  components: {
    CustomButton,
    EllipsisDropdown,
    Modal,
    PageBody,
    PageTitle,
  },
  data() {
    return {
      currentAction: "" as string,
      currentIndex: 0 as number,
    };
  },
  methods: {
    ...mapActions(useProductStore, ["listProducts", "destroyProduct"]),
    handleAction() {
      console.log("Action clicked");
    },
    handleActions(obj: any) {
      const product = this.products[obj.currentIndex];
      if (obj.action === "Update") {
        this.$router.push({
          name: "product.update",
          params: { id: product.id },
        });
      }
      this.currentAction = obj.action;
      this.currentIndex = obj.currentIndex;
    },
    async submitAction() {
      const action = this.currentAction;
      if (action === "Delete") {
        const product = this.products[this.currentIndex] as Product;
        if (product.id) {
          this.destroyProduct(product.id);
        }
      }
    },
  },
  computed: {
    ...mapState(useProductStore, ["products"]),
  },
  async mounted() {
    await this.listProducts();
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";
</style>
