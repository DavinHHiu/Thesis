<template>
  <page-title :title="$t('addressPage.list.title')" />
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
import { mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "AddressView",
  components: {
    PageTitle,
    PageBody,
    TabLayout,
  },
  data() {
    return {
      currentAction: "" as string,
      currentIndex: 0 as number,
      tabs: [
        { title: "Provinces", name: "province.list", path: "/provinces" },
        { title: "Districts", name: "district.list", path: "/districts" },
        { title: "Wards", name: "ward.list", path: "/wards" },
      ] as TabItem[],
    };
  },
  methods: {
    handleChangeTab(index: number): void {
      this.$router.push({ name: this.tabs[index].name });
    },
  },
  mounted() {
    this.$router.push({ name: this.tabs[0].name });
  },
});
</script>
