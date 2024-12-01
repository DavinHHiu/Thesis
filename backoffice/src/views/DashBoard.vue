<template>
  <page-title title="dashboardPage.title" />
  <page-body class="flex flex-col gap-[4rem]">
    <section class="flex flex-col gap-[3rem]">
      <select-field
        class="w-1/2 mt-[2rem]"
        v-model="period"
        :label="$t('dashboardPage.label.period')"
        :options="options"
        :value="period"
        @update:model-value="handleStatistics"
      />
      <loading-content v-if="loading" />
      <div v-else class="w-full flex gap-[2rem] flex-wrap">
        <card class="w-full h-[65rem]">
          <h2 class="section-title" v-text="'Revenue statistics'" />
          <bar-chart
            class="w-full h-full"
            :title="revenueTitle"
            :labels="revenueLabels"
            :label="revenueTitle"
            :data="revenueData"
          />
        </card>
      </div>
    </section>
    <section class="flex flex-col gap-[2rem]"></section>
  </page-body>
</template>

<script lang="ts">
import SelectField from "@/components/common/molecules/SelectField.vue";
import BarChart from "@/components/common/organisms/BarChart.vue";
import LineChart from "@/components/common/organisms/LineChart.vue";
import PieChart from "@/components/common/organisms/PieChart.vue";
import RadarChart from "@/components/common/organisms/RadarChart.vue";
import Card from "@/components/common/templates/Card.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import consts, { StatisticPeriodType } from "@/consts/consts";
import MainLayout from "@/layouts/MainLayout.vue";
import { useStatistic } from "@/stores/statistis";
import { OptionItem, Period } from "@/types/backoffice";
import { fmtDate } from "@/utils/date";
import {
  startOfWeek,
  endOfWeek,
  startOfMonth,
  endOfMonth,
  startOfYear,
  endOfYear,
  format,
} from "date-fns";
import { mapActions } from "pinia";

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
    SelectField,
  },
  data() {
    const options = Object.keys(consts.STATISTIC_PERIODS_DISPLAY).map((key) => {
      return {
        value: key,
        displayValue:
          consts.STATISTIC_PERIODS_DISPLAY[key as StatisticPeriodType],
      } as OptionItem;
    });
    return {
      loading: false,
      options,
      period: consts.STATISTIC_WEEK_PERIOD,
      revenueLabels: [],
      revenueData: [],
      revenueTitle: "",
    };
  },
  methods: {
    ...mapActions(useStatistic, ["fetchRevenueStatistic"]),
    async handleStatistics() {
      const now = new Date();
      let firstDate = "";
      let lastDate = "";

      if (this.period === consts.STATISTIC_WEEK_PERIOD) {
        firstDate = format(
          startOfWeek(now, { weekStartsOn: 1 }),
          this.$config.iso8601Format
        );
        lastDate = format(
          endOfWeek(now, { weekStartsOn: 1 }),
          this.$config.iso8601Format
        );
      } else if (this.period === consts.STATISTIC_MONTH_PERIOD) {
        firstDate = format(startOfMonth(now), this.$config.iso8601Format);
        lastDate = format(endOfMonth(now), this.$config.iso8601Format);
      } else {
        firstDate = format(startOfYear(now), this.$config.iso8601Format);
        lastDate = format(endOfYear(now), this.$config.iso8601Format);
      }

      const response = await this.fetchRevenueStatistic({
        start_date: firstDate,
        end_date: lastDate,
      } as Period);

      this.revenueLabels = Object.keys(response.data).map((label) => {
        return fmtDate(new Date(label));
      });
      this.revenueData = Object.values(response.data);
      this.revenueTitle = `Sales for ${this.period}`;
    },
  },
  async mounted() {
    this.loading = true;
    await this.handleStatistics();
    this.loading = false;
  },
};
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.section-title {
  font-size: $--font-base;
  font-weight: $--font-semibold;
}

::v-deep .card {
  padding: 2rem 4rem 4rem 4rem;
}
</style>
