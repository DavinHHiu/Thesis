<template>
  <page-title title="Add category" />
  <page-body>
    <card class="flex">
      <section class="info-wp flex flex-col gap-[4rem]">
        <text-field
          :value="currentCategory.name"
          label="Name"
          @update:modelValue="(newValue) => (currentCategory.name = newValue)"
        />
        <text-field
          :value="currentCategory.description"
          label="Description"
          @update:modelValue="
            (newValue) => (currentCategory.description = newValue)
          "
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
import UploadPreview from "@/components/common/molecules/UploadPreview.vue";
import Card from "@/components/common/templates/Card.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useCategory } from "@/stores/category";
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
    ...mapActions(useCategory, [
      "createCategory",
      "retrieveCategory",
      "updateCategory",
    ]),
    handleUpdate() {
      if (this.new) {
        this.createCategory(this.currentCategory);
      } else {
        this.updateCategory(this.currentCategory);
      }
      this.$router.push("/categories");
    },
  },
  computed: {
    ...mapState(useCategory, ["currentCategory"]),
  },
  mounted() {
    const id = this.$router.currentRoute._value.params.id;
    if (id) {
      this.retrieveCategory(id);
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
