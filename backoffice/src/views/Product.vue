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
            <td v-text="index + 1" />
            <td v-text="fmt(product.name)" />
            <td v-text="fmt(product.categories)" />
            <td>
              <badge-star :rating="fmt(product.rating)" />
            </td>
            <td class="text-ellipsis" v-text="fmt(product.description)" />
            <td class="text-ellipsis" v-text="fmt(product.summary)" />
            <td class="action-wrap">
              <ellipsis-dropdown
                @action="handleActions"
                :current-index="index"
                :dropdown-list="[
                  {
                    title: $t('productPage.dropdown[0].title'),
                    action: 'detail',
                  },
                  {
                    title: $t('productPage.dropdown[1].title'),
                    action: 'openModal',
                  },
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
import { fmt } from "@/utils/string";
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
      currentIndex: 0 as number,
    };
  },
  methods: {
    ...mapActions(useProductStore, ["listProducts", "destroyProduct"]),
    handleActions(obj: any) {
      const product = this.products[obj.currentIndex];
      if (obj.action === "detail") {
        this.$router.push({
          name: "product.update",
          params: { productId: product.id },
        });
      } else if (obj.action === "openModal") {
        const modal = this.$refs.deleteModal as InstanceType<typeof Modal>;
        modal.open();
      }
      this.currentIndex = obj.currentIndex;
    },
    async handleDelete() {
      const product = this.products[this.currentIndex] as Product;
      if (product.id) {
        this.destroyProduct(product.id);
      }
    },
    fmt,
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
