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
          <td v-text="index + 1" />
          <td v-text="fmt(productSku.sku)" />
          <td v-text="fmt(productSku.size.value)" />
          <td v-text="fmt(productSku.color.value)" />
          <td v-text="fmt(productSku.quantity)" />
          <td v-text="fmtAmount(productSku.price)" />
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
  <modal
    ref="deleteModal"
    id="deleteModal"
    title="Delete attribute"
    @confirm="handleDelete"
  >
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
import { fmtCur } from "@/utils/currency";
import { fmt } from "@/utils/string";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";
import { useI18n } from "vue-i18n";

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
      if (obj.action === "update") {
        this.$router.push({
          name: "product.sku.update",
          params: { productSkuId: productSku.id },
        });
      } else if (obj.action === "openModal") {
        const modal = this.$refs.deleteModal as InstanceType<typeof Modal>;
        modal.open();
      }
      this.currentIndex = obj.currentIndex;
    },
    async handleDelete() {
      const product = this.productSkus[this.currentIndex] as ProductSku;
      if (product.id) {
        this.destroyProductSku(product.id);
      }
    },
    fmtAmount(amount: number) {
      const { locale } = useI18n();
      return fmtCur(locale.value, amount);
    },
    fmt,
  },
  computed: {
    ...mapState(useProductSkuStore, ["productSkus"]),
  },
  async mounted() {
    const productId = this.$route.params.productId;
    await this.listProductSkus(productId as string);
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";
</style>
