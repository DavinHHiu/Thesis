<template>
  <page-title title="Products" />
  <page-body>
    <card class="h-[80vh] flex">
      <section class="upload-wp">
        <upload-preview
          :modelValue="product.cover"
          @update:model-value="(newValue) => (product.cover = newValue)"
        />
      </section>
      <section class="info-wp flex flex-col gap-[4rem]">
        <text-field
          :value="product.name"
          label="Product name"
          @update:model-value="(newValue) => (product.name = newValue)"
        />
        <text-field
          :value="product.sku"
          label="Product sku"
          @update:model-value="(newValue) => (product.sku = newValue)"
        />
        <text-field
          :value="product.price"
          label="Product price"
          @update:model-value="(newValue) => (product.price = newValue)"
        />
        <text-field
          :value="product.quantity"
          label="Product quantity"
          @update:model-value="(newValue) => (product.quantity = newValue)"
        />
        <div class="flex gap-[1rem]">
          <select-field
            :value="String(product?.color?.id || '')"
            class="flex-1"
            label="Color"
            :options="colorOptions"
            @update:model-value="selectColor"
          />
          <select-field
            :value="String(product?.size?.id || '')"
            class="flex-1"
            label="Size"
            :options="sizeOptions"
            @update:model-value="selectSize"
          />
          <select-field
            :value="String(product?.categories?.[0].id || '')"
            class="flex-1"
            label="Categories"
            :options="categorieOptions"
            @update:model-value="selectCategories"
          />
        </div>
        <text-field
          :value="product.description"
          label="Product description"
          @update:model-value="(newValue) => (product.description = newValue)"
        />
        <text-field
          :value="product.summary"
          label="Product summary"
          @update:model-value="(newValue) => (product.summary = newValue)"
        />
        <custom-button class="w-[15rem]" @click="handleUpdate"
          >Update</custom-button
        >
      </section>
    </card>
  </page-body>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import SelectField from "@/components/common/molecules/SelectField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import UploadPreview from "@/components/common/molecules/UploadPreview.vue";
import Card from "@/components/common/templates/Card.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useProductStore } from "@/stores/product";
import { useProductAttributeStore } from "@/stores/productAttribute";
import { useSubCategoryStore } from "@/stores/subcategory";
import { OptionItem } from "@/types/backoffice";
import { ProductAttribute, SubCategory } from "@/types/worker";
import _ from "lodash";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "ProductUpdateView",
  components: {
    Card,
    CustomButton,
    PageBody,
    PageTitle,
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
    ...mapActions(useProductStore, [
      "createProduct",
      "retrieveProduct",
      "updateProduct",
    ]),
    ...mapActions(useProductAttributeStore, ["listProductAttributes"]),
    ...mapActions(useSubCategoryStore, ["listSubCategories"]),
    handleUpdate() {
      if (this.new) {
        this.createProduct(this.product);
      } else {
        this.updateProduct(this.product);
      }
      this.$router.push("/products");
    },
    selectColor(value: string) {
      const color = _.find(
        this.colors,
        (color) => color.id === Number(value)
      ) as ProductAttribute;
      this.product.color = color;
    },
    selectSize(value: number) {
      const size = _.find(
        this.sizes,
        (size) => size.id === Number(value)
      ) as ProductAttribute;
      this.product.size = size;
    },
    selectCategories(value: number) {
      const category = _.find(
        this.subcategories,
        (category) => category.id === Number(value)
      ) as SubCategory;
      this.product.categories[0] = category;
    },
  },
  computed: {
    ...mapState(useProductStore, ["product"]),
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
  },
  async mounted() {
    await this.listProductAttributes();
    await this.listSubCategories();
    const id = this.$router.currentRoute._value.params.id;
    if (id) {
      await this.retrieveProduct(id);
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
