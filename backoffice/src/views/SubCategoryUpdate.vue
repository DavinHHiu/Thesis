<template>
  <page-body>
    <card class="flex">
      <section class="info-wp flex flex-col gap-[4rem]">
        <text-field
          :value="subcategory.name"
          :label="$t('inputLabel.common.name')"
          @update:modelValue="(newValue) => (subcategory.name = newValue)"
        />
        <text-field
          :value="subcategory.description"
          :label="$t('inputLabel.common.description')"
          @update:modelValue="
            (newValue) => (subcategory.description = newValue)
          "
        />
        <select-field
          :value="String(subcategory?.category?.id || '')"
          :label="$t('inputLabel.subcategory.category')"
          :options="options"
          @update:modelValue="selectCategory"
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
import Card from "@/components/common/templates/Card.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import { useCategoryStore } from "@/stores/category";
import { useSubCategoryStore } from "@/stores/subcategory";
import { OptionItem } from "@/types/backoffice";
import { Category, SubCategory } from "@/types/worker";
import _ from "lodash";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "CategoryUpdateView",
  components: {
    Card,
    CustomButton,
    PageBody,
    TextField,
    SelectField,
  },
  data() {
    return {
      new: true as boolean,
    };
  },
  methods: {
    ...mapActions(useCategoryStore, ["listCategories"]),
    ...mapActions(useSubCategoryStore, [
      "createSubCategory",
      "retrieveSubCategory",
      "resetSubCategory",
    ]),
    selectCategory(value: string) {
      const category = _.find(
        this.categories,
        (category) => category.id === Number(value)
      ) as Category;
      this.subcategory.category = category;
    },
    handleUpdate() {
      if (this.new) {
        this.createSubCategory(this.subcategory);
        this.$router.push("/sub-categories");
      }
    },
  },
  computed: {
    ...mapState(useCategoryStore, ["categories"]),
    ...mapState(useSubCategoryStore, ["subcategory"]),
    options(): OptionItem[] {
      return _.map(this.categories, (category) => {
        return {
          displayValue: category.name,
          value: String(category.id),
        };
      });
    },
    textButton() {
      return this.new
        ? this.$t("buttonLabel.add")
        : this.$t("buttonLabel.update");
    },
  },
  mounted() {
    this.listCategories();
    const id = this.$router.currentRoute.value.params.subcategoryId;
    if (id) {
      this.retrieveSubCategory(Number(id));
      this.new = false;
    }
  },
  beforeRouteLeave() {
    this.resetSubCategory();
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
