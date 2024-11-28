<template>
  <page-title title="dashboardPage.title" />
  <page-body>
    <div class="w-full flex gap-[2rem] flex-wrap">
      <card class="w-1/2 h-[40rem]">
        <line-chart class="w-full h-full" />
      </card>
      <card class="w-1/2 h-[40rem]">
        <bar-chart class="w-full h-full" />
      </card>
      <card>
        <pie-chart class="w-full h-full" />
      </card>
    </div>
  </page-body>
</template>

<script lang="ts">
import BarChart from "@/components/common/organisms/BarChart.vue";
import LineChart from "@/components/common/organisms/LineChart.vue";
import PieChart from "@/components/common/organisms/PieChart.vue";
import RadarChart from "@/components/common/organisms/RadarChart.vue";
import Card from "@/components/common/templates/Card.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import MainLayout from "@/layouts/MainLayout.vue";

export default {
  name: "HomePage",
  components: {
    BarChart,
    Card,
    MainLayout,
    PageBody,
    PageTitle,
    PieChart,
    LineChart,
    RadarChart,
  },
};
</script>
