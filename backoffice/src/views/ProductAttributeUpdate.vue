<template>
  <page-title :title="pageTitle" />
  <page-body>
    <card class="flex">
      <section class="info-wp flex flex-col gap-[4rem]">
        <text-field
          :label="$t('inputLabel.productAttribute.type')"
          :value="productAttribute.type"
          @update:modelValue="(newValue) => (productAttribute.type = newValue)"
        />
        <text-field
          :label="$t('inputLabel.productAttribute.value')"
          :value="productAttribute.value"
          @update:modelValue="(newValue) => (productAttribute.value = newValue)"
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
      "resetProductAttribute",
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
    textButton() {
      return this.new
        ? this.$t("buttonLabel.add")
        : this.$t("buttonLabel.update");
    },
    pageTitle() {
      return this.new
        ? this.$t("productAttributePage.add.title")
        : this.$t("productAttributePage.update.title");
    },
  },
  mounted() {
    const id = this.$router.currentRoute.value.params.id;
    if (id) {
      this.retrieveProductAttribute(Number(id));
      this.new = false;
    }
  },
  beforeRouteLeave() {
    this.resetProductAttribute();
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
