<template>
  <card class="flex">
    <section class="upload-wp">
      <upload-preview
        :modelValue="productSku.images"
        @update:model-value="(newValue) => (productSku.images = newValue)"
      />
    </section>
    <section class="info-wp flex flex-col gap-[4rem]">
      <text-field
        :label="$t('inputLabel.product.sku')"
        :value="productSku.sku"
        @update:model-value="(newValue) => (productSku.sku = newValue)"
      />
      <text-field
        :label="$t('inputLabel.product.price')"
        :value="productSku.price"
        @update:model-value="(newValue) => (productSku.price = newValue)"
      />
      <text-field
        :label="$t('inputLabel.product.quantity')"
        :value="productSku.quantity"
        @update:model-value="(newValue) => (productSku.quantity = newValue)"
      />
      <div class="flex gap-[1rem]">
        <select-field
          class="flex-1"
          :label="$t('inputLabel.product.color')"
          :value="String(productSku?.color?.id || '')"
          :options="colorOptions"
          @update:model-value="selectColor"
        />
        <select-field
          class="flex-1"
          :label="$t('inputLabel.product.size')"
          :value="String(productSku?.size?.id || '')"
          :options="sizeOptions"
          @update:model-value="selectSize"
        />
      </div>
      <custom-button
        class="w-[15rem]"
        @click="handleUpdate"
        v-text="textButton"
      />
    </section>
  </card>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import SelectField from "@/components/common/molecules/SelectField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import UploadPreview from "@/components/common/molecules/UploadPreview.vue";
import Card from "@/components/common/templates/Card.vue";
import { useProductAttributeStore } from "@/stores/productAttribute";
import { useProductSkuStore } from "@/stores/productSku";
import { useSubCategoryStore } from "@/stores/subcategory";
import { OptionItem } from "@/types/backoffice";
import { ProductAttribute } from "@/types/worker";
import _ from "lodash";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "ProductUpdateView",
  components: {
    Card,
    CustomButton,
    TextField,
    SelectField,
    UploadPreview,
  },
  data() {
    return {
      new: true as boolean,
      colors: [] as ProductAttribute[],
      sizes: [] as ProductAttribute[],
    };
  },
  methods: {
    ...mapActions(useProductSkuStore, [
      "createProductSku",
      "retrieveProductSku",
      "updateProductSku",
    ]),
    ...mapActions(useProductAttributeStore, ["listProductAttributes"]),
    ...mapActions(useSubCategoryStore, ["listSubCategories"]),
    handleUpdate() {
      if (this.new) {
        this.createProductSku(this.productSku);
      } else {
        this.updateProductSku(this.productSku);
      }
      this.$router.push({ name: "product.skus.list" });
    },
    selectColor(value: string) {
      const color = _.find(
        this.colors,
        (color) => color.id === Number(value)
      ) as ProductAttribute;
      this.productSku.color = color;
    },
    selectSize(value: number) {
      const size = _.find(
        this.sizes,
        (size) => size.id === Number(value)
      ) as ProductAttribute;
      this.productSku.size = size;
    },
  },
  computed: {
    ...mapState(useProductSkuStore, ["productSku"]),
    ...mapState(useProductAttributeStore, ["productAttributes"]),
    ...mapState(useSubCategoryStore, ["subcategories"]),
    colorOptions(): OptionItem[] {
      return _.map(this.colors, (color) => {
        return {
          value: String(color.id),
          displayValue: color.value,
        };
      });
    },
    sizeOptions(): OptionItem[] {
      return _.map(this.sizes, (size) => {
        return {
          value: String(size.id),
          displayValue: size.value,
        };
      });
    },
    categorieOptions(): OptionItem[] {
      return _.map(this.subcategories, (subcategory) => {
        return {
          value: String(subcategory.id),
          displayValue: subcategory.name,
        };
      });
    },
    textButton() {
      return this.new
        ? this.$t("buttonLabel.add")
        : this.$t("buttonLabel.update");
    },
  },
  async mounted() {
    await this.listProductAttributes();
    await this.listSubCategories();
    const id = this.$router.currentRoute.value.params.productSkuId;
    const productId = this.$router.currentRoute.value.params.productId;
    if (productId) {
      this.productSku.product_id = productId as string;
    }
    if (id) {
      await this.retrieveProductSku(id as string);
      this.new = false;
    }
    this.colors = _.filter(
      this.productAttributes,
      (attribute) => attribute.type === "Color"
    );
    this.sizes = _.filter(
      this.productAttributes,
      (attribute) => attribute.type === "Size"
    );
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.upload-wp {
  padding: 2rem 4rem;
  color: $--gray-color-700;
}
.info-wp {
  flex: 1;
  padding: 2rem 4rem;
}
</style>
