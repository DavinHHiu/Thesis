<template>
  <div>
    <Pie :data="chartData" :options="chartOptions" />
  </div>
</template>

<script lang="ts">
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement } from "chart.js";
import { defineComponent } from "vue";
import { Pie } from "vue-chartjs";

ChartJS.register(Title, Tooltip, Legend, ArcElement);

export default defineComponent({
  name: "PieChart",
  components: {
    Pie,
  },
  data() {
    return {
      chartData: {
        labels: ["Red", "Blue", "Yellow"],
        datasets: [
          {
            data: [300, 50, 100],
            backgroundColor: ["#FF6347", "#4682B4", "#FFD700"],
            hoverBackgroundColor: ["#FF0000", "#0000FF", "#FFFF00"],
          },
        ],
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
          legend: {
            display: true,
            position: "top" as const,
          },
          title: {
            display: true,
            text: "Sales 2024",
          },
        },
      },
    };
  },
});
</script>
