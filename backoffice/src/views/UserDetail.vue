<template>
  <page-title :title="pageTitle" />
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
  name: "UserDetailView",
  components: {
    PageBody,
    PageTitle,
    TabLayout,
  },
  data() {
    return {
      userId: "",
      pageTitle: "User",
      tabs: [
        { title: "User", path: "update" },
        { title: "Addresses", path: "addresses" },
        { title: "Cart", path: "cart" },
        { title: "Order", path: "order" },
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

.upload-wp {
  padding: 2rem 4rem;
  color: $--gray-color-700;
}

.info-wp {
  flex: 1;
  padding: 2rem 4rem;
}
</style>
