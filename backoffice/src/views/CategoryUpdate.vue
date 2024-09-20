<template>
  <page-title v-if="new" :title="pageTitle" />
  <page-body>
    <card class="flex">
      <section class="info-wp flex flex-col gap-[4rem]">
        <text-field
          :label="$t('inputLabel.common.name')"
          :value="category.name"
          @update:modelValue="(newValue) => (category.name = newValue)"
        />
        <text-field
          :label="$t('inputLabel.common.description')"
          :value="category.description"
          @update:modelValue="(newValue) => (category.description = newValue)"
        />
        <custom-button
          @click="handleUpdate"
          class="w-[15rem]"
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
import { useCategoryStore } from "@/stores/category";
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
    UploadPreview,
  },
  data() {
    return {
      new: true as boolean,
    };
  },
  methods: {
    ...mapActions(useCategoryStore, [
      "createCategory",
      "retrieveCategory",
      "updateCategory",
      "resetCategory",
    ]),
    handleUpdate() {
      if (this.new) {
        this.createCategory(this.category);
      } else {
        this.updateCategory(this.category);
      }
      this.$router.push("/categories");
    },
  },
  computed: {
    ...mapState(useCategoryStore, ["category"]),
    textButton() {
      return this.new
        ? this.$t("buttonLabel.add")
        : this.$t("buttonLabel.update");
    },
    pageTitle() {
      return this.new
        ? this.$t("categoryPage.add.title")
        : this.$t("categoryPage.update.title");
    },
  },
  mounted() {
    const id = this.$router.currentRoute.value.params.categoryId;
    if (id) {
      this.retrieveCategory(Number(id));
      this.new = false;
    }
  },
  beforeRouteLeave() {
    this.resetCategory();
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
