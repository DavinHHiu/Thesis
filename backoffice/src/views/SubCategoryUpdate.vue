<template>
  <page-body>
    <card class="flex">
      <section class="info-wp flex flex-col gap-[4rem]">
        <text-field
          :value="subcategory.name"
          label="inputLabel.common.name"
          @update:modelValue="(newValue) => (subcategory.name = newValue)"
        />
        <text-field
          :value="subcategory.description"
          label="inputLabel.common.description"
          @update:modelValue="
            (newValue) => (subcategory.description = newValue)
          "
        />
        <select-field
          :value="String(subcategory?.category_id || '')"
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
      isNew: true as boolean,
    };
  },
  methods: {
    ...mapActions(useCategoryStore, ["listCategories"]),
    ...mapActions(useSubCategoryStore, [
      "createSubCategory",
      "retrieveSubCategory",
      "resetSubCategory",
      "updateSubCategory",
    ]),
    selectCategory(value: string) {
      const category = _.find(
        this.categories,
        (category) => category.id === Number(value)
      ) as Category;
      if (category && category.id) {
        this.subcategory.category_id = category.id;
      }
    },
    handleUpdate() {
      this.isNew
        ? this.createSubCategory(this.subcategory)
        : this.updateSubCategory(this.subcategory);
      this.$router.push({ name: "subcategory.list" });
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
      return this.isNew
        ? this.$t("buttonLabel.add")
        : this.$t("buttonLabel.update");
    },
  },
  mounted() {
    this.listCategories();
    const id = this.$route.params.subcategoryId;
    if (id) {
      this.retrieveSubCategory(Number(id));
      this.isNew = false;
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
