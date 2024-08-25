<template>
  <page-title :title="pageTitle" />
  <page-body>
    <card class="h-[32vh] flex">
      <section class="info-wp flex flex-col justify-between">
        <text-field
          :value="attribute.type"
          label="Type"
          @update:modelValue="(newValue) => (attribute.type = newValue)"
        />
        <text-field
          :value="attribute.value"
          label="Value"
          @update:modelValue="(newValue) => (attribute.value = newValue)"
        />
        <custom-button @click="handleUpdate" class="w-[15rem]">
          {{ this.new ? "Add" : "Update" }}
        </custom-button>
      </section>
    </card>
  </page-body>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import Card from "@/components/common/templates/Card.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useProductAttributeStore } from "@/stores/useProductAttributeStore";
import { mapActions } from "pinia";
import { defineComponent } from "vue";
import { useRouter } from "vue-router";

export default defineComponent({
  name: "ProductAttributeUpdateView",
  components: {
    Card,
    CustomButton,
    PageBody,
    PageTitle,
    TextField,
  },
  data() {
    return {
      new: true as boolean,
      attribute: {} as ProductAttribute,
    };
  },
  methods: {
    ...mapActions(useProductAttributeStore, [
      "createProductAttribute",
      "updateProductAttribute",
      "retrieveProductAttribute",
    ]),
    handleUpdate() {
      if (this.new) {
        const { type, value } = this.$data.attribute;
        this.createProductAttribute({ type, value });
      } else {
        this.updateProductAttribute(this.attribute);
      }
      this.$router.push("/product-attributes");
    },
  },
  computed: {
    pageTitle() {
      return this.new ? "Create Product Attribute" : "Update Product Attribute";
    },
  },
  async mounted() {
    const id = this.$router.currentRoute._value.params.id;
    if (id) {
      const response = await this.retrieveProductAttribute(id);
      this.attribute = response.data;
      this.new = false;
      console.log(response);
    }
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.info-wp {
  width: 100%;
  padding: 2rem 4rem;
}
</style>
