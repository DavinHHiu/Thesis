<template>
  <page-title :title="pageTitle" />
  <page-body>
    <card class="flex">
      <section class="info-wp flex flex-col gap-[4rem]">
        <text-field
          :value="productAttribute.type"
          label="Type"
          @update:modelValue="(newValue) => (productAttribute.type = newValue)"
        />
        <text-field
          :value="productAttribute.value"
          label="Value"
          @update:modelValue="(newValue) => (productAttribute.value = newValue)"
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
import TextField from "@/components/common/molecules/TextField.vue";
import Card from "@/components/common/templates/Card.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useProductAttributeStore } from "@/stores/productAttribute";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

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
        this.createProductAttribute(this.productAttribute);
      } else {
        this.updateProductAttribute(this.productAttribute);
      }
      this.$router.push("/product-attributes");
    },
  },
  computed: {
    ...mapState(useProductAttributeStore, ["productAttribute"]),
    pageTitle() {
      return this.new ? "Create Product Attribute" : "Update Product Attribute";
    },
  },
  async mounted() {
    const id = this.$router.currentRoute._value.params.id;
    if (id) {
      this.retrieveProductAttribute(id);
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
