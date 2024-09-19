<template>
  <page-title v-if="new" :title="pageTitle" />
  <page-body>
    <card class="flex">
      <section class="info-wp flex flex-col gap-[4rem]">
        <text-field
          :label="$t('inputLabel.common.name')"
          :value="product.name"
          @update:model-value="(newValue) => (product.name = newValue)"
        />
        <div class="flex gap-[1rem]">
          <select-field
            class="flex-1"
            :label="$t('inputLabel.product.categories')"
            :value="String(product?.categories?.[0].id || '')"
            :options="categorieOptions"
            @update:model-value="selectCategories"
          />
        </div>
        <text-field
          :label="$t('inputLabel.common.description')"
          :value="product.description"
          @update:model-value="(newValue) => (product.description = newValue)"
        />
        <text-field
          :label="$t('inputLabel.product.summary')"
          :value="product.summary"
          @update:model-value="(newValue) => (product.summary = newValue)"
        />
        <custom-button
          class="w-[15rem]"
          @click="handleUpdate"
          v-text="textButton"
        />
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
      this.$router.push({ name: "product.list" });
    },
    selectCategories(value: number) {
      const category = _.find(
        this.subcategories,
        (category) => category.id === Number(value)
      ) as SubCategory;
      this.product.categories ??= [];
      this.product.categories[0] = category;
    },
  },
  computed: {
    ...mapState(useProductStore, ["product"]),
    ...mapState(useProductAttributeStore, ["productAttributes"]),
    ...mapState(useSubCategoryStore, ["subcategories"]),
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
    pageTitle() {
      return this.new
        ? this.$t("productPage.addProduct.title")
        : this.$t("productPage.updateProduct.title");
    },
  },
  async mounted() {
    await this.listProductAttributes();
    await this.listSubCategories();
    const id = this.$router.currentRoute.value.params.productId;
    if (id) {
      await this.retrieveProduct(id as string);
      this.new = false;
    }
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.info-wp {
  flex: 1;
  padding: 4rem 4rem 2rem;
}
</style>
