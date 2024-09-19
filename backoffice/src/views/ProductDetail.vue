<template>
  <page-title :title="$t('productPage.productDetail.title')" />
  <page-body>
    <tab-layout
      :cur-path-name="curPathName"
      :tabs="tabs"
      @change:tab="handleChangeTab"
    />
    <router-view />
  </page-body>
</template>

<script lang="ts">
import TabLayout from "@/components/common/molecules/TabLayout.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { TabItem } from "@/types/backoffice";
import _ from "lodash";
import { defineComponent } from "vue";

export default defineComponent({
  name: "ProductDetail",
  components: {
    PageBody,
    PageTitle,
    TabLayout,
  },
  data() {
    return {
      tabs: [
        { title: "Product Detail", name: "product.update", path: "/detail" },
        {
          title: "Product SKUs",
          name: "product.skus.list",
          path: "/product-skus",
        },
      ] as TabItem[],
      curPathName: "" as string,
    };
  },
  methods: {
    handleChangeTab(index: number): void {
      this.$router.push({ name: this.tabs[index].name });
    },
  },
  mounted() {
    this.curPathName = this.$router.currentRoute.value.name as string;
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.upload-wp {
  padding: 2rem 4rem;
  color: $--gray-color-700;
}

.info-wp {
  flex: 1;
  padding: 2rem 4rem;
}
</style>
