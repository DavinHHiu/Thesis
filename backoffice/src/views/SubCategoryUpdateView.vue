<template>
  <page-title title="Add category" />
  <page-body>
    <card class="flex">
      <section class="info-wp flex flex-col gap-[4rem]">
        <text-field
          :value="subcategory.name"
          label="Name"
          @update:modelValue="(newValue) => (subcategory.name = newValue)"
        />
        <text-field
          :value="subcategory.description"
          label="Description"
          @update:modelValue="
            (newValue) => (subcategory.description = newValue)
          "
        />
        <select-field
          :value="String(subcategory?.category?.id || '')"
          label="Category"
          :options="options"
          @update:modelValue="selectCategory"
        />
        <custom-button @click="handleUpdate" class="w-[15rem]">
          {{ "Update" }}
        </custom-button>
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
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useCategory } from "@/stores/category";
import { useSubCategoryStore } from "@/stores/subcategory";
import { OptionItem } from "@/types/backoffice";
import { Category } from "@/types/worker";
import _ from "lodash";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "CategoryUpdateView",
  components: {
    Card,
    CustomButton,
    PageBody,
    PageTitle,
    TextField,
    SelectField,
  },
  data() {
    return {
      new: true as boolean,
    };
  },
  methods: {
    ...mapActions(useCategory, ["listCategories"]),
    ...mapActions(useSubCategoryStore, [
      "createSubCategory",
      "retrieveSubCategory",
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
    ...mapState(useCategory, ["categories"]),
    ...mapState(useSubCategoryStore, ["subcategory"]),
    options(): OptionItem[] {
      return _.map(this.categories, (category) => {
        return {
          displayValue: category.name,
          value: String(category.id),
        };
      });
    },
  },
  mounted() {
    this.listCategories();
    const id = this.$router.currentRoute._value.params.id;
    if (id) {
      this.retrieveSubCategory(id);
      this.new = false;
    }
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.info-wp {
  width: 100%;
  padding: 4rem;
}
</style>
