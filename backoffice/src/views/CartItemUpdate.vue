<template>
  <page-body>
    <card class="flex">
      <section class="info-wp flex flex-col gap-[4rem]">
        <div class="flex gap-[1rem]">
          <select-field
            class="flex-1"
            :label="$t('inputLabel.cartItem.product')"
            :value="productDetail.id"
            :options="productOptions"
            @update:model-value="selectProduct"
          />
          <select-field
            class="flex-1"
            :class="{ invisible: !productDetail.skus }"
            :label="$t('inputLabel.cartItem.productSku')"
            :value="cartItem?.product_sku?.id"
            :options="productSkuOptions"
            @update:model-value="selectProductSku"
          />
        </div>
        <text-field
          v-if="cartItem?.product_sku?.id"
          :label="$t('inputLabel.product.price')"
          :value="cartItem.product_sku?.price"
          @update:model-value="(newValue) => (cartItem.quantity = newValue)"
        />
        <text-field
          :label="$t('inputLabel.cartItem.quantity')"
          :value="cartItem.quantity"
          @update:model-value="(newValue) => (cartItem.quantity = newValue)"
        />
        <text-field
          v-if="cartItem.quantity"
          :label="$t('inputLabel.cartItem.subTotal')"
          :value="cartItem.product_sku?.price * cartItem.quantity"
          @update:model-value="(newValue) => (cartItem.quantity = newValue)"
          :disabled="true"
        />
        <custom-form-button
          :text-button="textButton"
          @update="handleUpdate"
          @back="handleBack"
        />
      </section>
    </card>
  </page-body>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import CustomFormButton from "@/components/common/molecules/CustomFormButton.vue";
import SelectField from "@/components/common/molecules/SelectField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import UploadPreview from "@/components/common/molecules/UploadPreview.vue";
import Card from "@/components/common/templates/Card.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import { useCartItemStore } from "@/stores/cartItem";
import { useProductStore } from "@/stores/product";
import { useUserStore } from "@/stores/user";
import { OptionItem } from "@/types/backoffice";
import { ProductDetails, ProductSkuDetail } from "@/types/worker";
import _ from "lodash";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "UserUpdateView",
  components: {
    Card,
    CustomButton,
    CustomFormButton,
    PageBody,
    TextField,
    SelectField,
    UploadPreview,
  },
  data() {
    return {
      new: true as boolean,
      productDetail: {} as ProductDetails,
    };
  },
  methods: {
    ...mapActions(useUserStore, ["listUsers"]),
    ...mapActions(useProductStore, ["listProductsDisplay"]),
    ...mapActions(useCartItemStore, [
      "createCartItem",
      "retrieveCartItem",
      "updateCartItem",
      "resetCartItem",
    ]),
    async handleUpdate() {
      if (this.new) {
        this.createCartItem(this.cartItem);
      } else {
        await this.updateCartItem(this.cartItem);
      }
      this.$router.push({ name: "cart.items.list" });
    },
    handleBack() {
      this.$router.push({ name: "cart.items.list" });
    },
    selectProduct(productId: string) {
      this.productDetail = _.find(
        this.productsDetails,
        (product) => product.id === productId
      ) as ProductDetails;
      this.cartItem.product_sku = {} as ProductSkuDetail;
    },
    selectProductSku(skuId: string) {
      let productSkuDetail = _.find(
        this.productDetail.skus,
        (sku) => sku.id === skuId
      ) as ProductSkuDetail;
      this.cartItem.product_sku = productSkuDetail;
    },
  },
  computed: {
    ...mapState(useCartItemStore, ["cartItem"]),
    ...mapState(useProductStore, ["productsDetails"]),
    ...mapState(useUserStore, ["users"]),
    productOptions(): OptionItem[] {
      const users = _.map(this.productsDetails, (product) => {
        return {
          value: String(product.id),
          displayValue: product.name,
        };
      });
      return users;
    },
    productSkuOptions(): OptionItem[] {
      const skus = _.map(this.productDetail.skus, (sku) => {
        return {
          image: sku?.images?.[0]?.image,
          value: String(sku.id),
          displayValue: `Size: ${sku.size.value} Color: ${sku.color.value}`,
        };
      });
      return skus;
    },
    textButton() {
      return this.new
        ? this.$t("buttonLabel.add")
        : this.$t("buttonLabel.update");
    },
    pageTitle() {
      return this.new
        ? this.$t("cartPage.add.title")
        : this.$t("cartPage.update.title");
    },
  },
  async mounted() {
    const cartId = this.$router.currentRoute.value.params.cartId;
    const cartItemId = this.$router.currentRoute.value.params.cartItemId;
    await this.listProductsDisplay();
    if (cartItemId) {
      await this.retrieveCartItem(cartItemId as string);
      this.productDetail = _.find(
        this.productsDetails,
        (product) => product.id === this.cartItem.product_sku.product.id
      ) as ProductDetails;
      this.new = false;
    }
    this.cartItem.cart_id = cartId as string;
  },
  beforeRouteLeave() {
    this.resetCartItem();
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.info-wp {
  width: 100%;
  padding: 4rem 4rem 2rem;
}
</style>
