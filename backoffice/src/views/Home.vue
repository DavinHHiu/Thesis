<template>
  <page-title title="Home page" />
  <page-body>
    <card>{{ $t("home.me.again") }}</card>
  </page-body>
</template>

<script lang="ts">
import Card from "@/components/common/templates/Card.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import MainLayout from "@/layouts/MainLayout.vue";

export default {
  name: "HomePage",
  components: {
    Card,
    MainLayout,
    PageBody,
    PageTitle,
  },
};
</script>
