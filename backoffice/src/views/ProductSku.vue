<template>
  <header-action :current-route="$t('productSkuPage.add.name')" />
  <table class="w-full mt-[2rem] overflow-hidden">
    <thead>
      <tr>
        <th>No.</th>
        <th>Sku</th>
        <th>Size</th>
        <th>Color</th>
        <th>Quantity</th>
        <th>Price</th>
      </tr>
    </thead>
    <tbody>
      <template v-for="(productSku, index) in productSkus" :key="index">
        <tr :class="{ odd: index % 2 == 0 }">
          <td>{{ index + 1 }}</td>
          <td v-text="productSku.sku" />
          <td v-text="productSku.size.value" />
          <td v-text="productSku.color.value" />
          <td v-text="productSku.quantity" />
          <td v-text="productSku.price" />
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
  <modal id="deleteModal" title="Delete attribute" @confirm="submitAction">
    <span v-text="$t('productSkuPage.modalDelete.title')" />
  </modal>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import EllipsisDropdown from "@/components/common/molecules/EllipsisDropdown.vue";
import HeaderAction from "@/components/common/molecules/HeaderAction.vue";
import Modal from "@/components/common/molecules/Modal.vue";
import { useProductSkuStore } from "@/stores/productSku";
import { ProductSku } from "@/types/worker";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "ProductSkuView",
  components: {
    CustomButton,
    EllipsisDropdown,
    Modal,
    HeaderAction,
  },
  data() {
    return {
      currentAction: "" as string,
      currentIndex: 0 as number,
    };
  },
  methods: {
    ...mapActions(useProductSkuStore, ["listProductSkus", "destroyProductSku"]),
    handleAction() {
      console.log("Action clicked");
    },
    handleActions(obj: any) {
      const productSku = this.productSkus[obj.currentIndex];
      if (obj.action === "Update") {
        this.$router.push({
          name: "product.sku.update",
          params: { productSkuId: productSku.id },
        });
      }
      this.currentAction = obj.action;
      this.currentIndex = obj.currentIndex;
    },
    async submitAction() {
      const action = this.currentAction;
      if (action === "Delete") {
        const product = this.productSkus[this.currentIndex] as ProductSku;
        if (product.id) {
          this.destroyProductSku(product.id);
        }
      }
    },
  },
  computed: {
    ...mapState(useProductSkuStore, ["productSkus"]),
  },
  async mounted() {
    await this.listProductSkus();
    console.log(this.productSkus);
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";
</style>
