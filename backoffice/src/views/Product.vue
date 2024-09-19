<template>
  <page-title :title="$t('productPage.productList.title')" />
  <page-body>
    <header-action :current-route="$t('productPage.addProduct.name')" />
    <table class="w-full mt-[2rem] overflow-hidden">
      <thead>
        <tr>
          <th>No.</th>
          <th>Name</th>
          <th>Categories</th>
          <th>Rating</th>
          <th>Description</th>
          <th>Summary</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="(product, index) in products" :key="index">
          <tr :class="{ odd: index % 2 == 0 }">
            <td>{{ index + 1 }}</td>
            <td v-text="product.name" />
            <td v-text="product.categories[0].name" />
            <td>
              <badge-star :rating="product.rating ? product.rating : 0" />
            </td>
            <td class="text-ellipsis" v-text="product.description" />
            <td class="text-ellipsis" v-text="product.summary" />
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
    <span v-text="$t('productPage.modalDelete.title')" />
  </modal>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import BadgeStar from "@/components/common/molecules/BadgeStar.vue";
import EllipsisDropdown from "@/components/common/molecules/EllipsisDropdown.vue";
import HeaderAction from "@/components/common/molecules/HeaderAction.vue";
import Modal from "@/components/common/molecules/Modal.vue";
import RatingStar from "@/components/common/molecules/RatingStar.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useProductStore } from "@/stores/product";
import { Product } from "@/types/worker";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "ProductView",
  components: {
    BadgeStar,
    CustomButton,
    EllipsisDropdown,
    Modal,
    HeaderAction,
    PageBody,
    PageTitle,
    RatingStar,
  },
  data() {
    return {
      currentAction: "" as string,
      currentIndex: 0 as number,
    };
  },
  methods: {
    ...mapActions(useProductStore, ["listProducts", "destroyProduct"]),
    handleActions(obj: any) {
      const product = this.products[obj.currentIndex];
      if (obj.action === "Detail") {
        this.$router.push({
          name: "product.update",
          params: { productId: product.id },
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

.text-ellipsis {
  max-width: 20rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
