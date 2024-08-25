<template>
  <page-title title="Products" />
  <page-body>
    <card class="h-[80vh] flex">
      <section class="upload-wp">
        <upload-preview />
      </section>
      <section class="info-wp flex flex-col gap-[4rem]">
        <text-field label="Product name" placeholder="Enter product name..." />
        <text-field label="Product sku" placeholder="Enter product name..." />
        <text-field label="Product price" placeholder="Enter product name..." />
        <text-field
          label="Product quantity"
          placeholder="Enter product name..."
        />
        <div class="flex gap-[1rem]">
          <select-field class="flex-1" label="Color" />
          <select-field class="flex-1" label="Size" />
          <select-field class="flex-1" label="Categories" />
        </div>
        <text-field
          label="Product description"
          placeholder="Enter product name..."
        />
        <text-field
          label="Product summary"
          placeholder="Enter product name..."
        />
        <custom-button class="w-[15rem]">Update</custom-button>
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
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.upload-wp {
  width: 25%;
  padding: 2rem 4rem;
  color: $--gray-color-700;
}
.info-wp {
  width: 75%;
  padding: 2rem 4rem;
}
</style>
