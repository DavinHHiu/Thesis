<template>
  <page-title :title="$t('cartPage.detail.title')" />
  <page-body>
    <tab-layout :tabs="tabs" @change:tab="handleChangeTab" />
    <router-view />
  </page-body>
</template>

<script lang="ts">
import TabLayout from "@/components/common/molecules/TabLayout.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { TabItem } from "@/types/backoffice";
import { defineComponent } from "vue";

export default defineComponent({
  name: "CartDetailView",
  components: {
    PageBody,
    PageTitle,
    TabLayout,
  },
  data() {
    return {
      userId: "",
      pageTitle: "Cart Detail",
      tabs: [
        { title: "Cart Detail", name: "cart.update", path: "detail" },
        { title: "Cart Items", name: "cart.items.list", path: "cart-items" },
      ] as TabItem[],
    };
  },
  methods: {
    handleChangeTab(index: number): void {
      this.pageTitle = this.tabs[index].title;
      this.$router.push({ name: this.tabs[index].name });
    },
  },
  computed: {},
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";
</style>
