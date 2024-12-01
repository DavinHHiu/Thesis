<template>
  <div>
    <Bar :data="chartData" :options="chartOptions" />
  </div>
</template>

<script lang="ts">
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  LinearScale,
  CategoryScale,
} from "chart.js";
import { defineComponent, PropType } from "vue";
import { Bar } from "vue-chartjs";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  LinearScale,
  CategoryScale
);

export default defineComponent({
  name: "BarChart",
  props: {
    title: {
      type: String,
      required: false,
    },
    label: {
      type: String,
      required: false,
    },
    labels: {
      type: Array,
      required: true,
    },
    data: {
      type: Array as PropType<number[]>,
      required: true,
      default: [],
    },
  },
  components: {
    Bar,
  },
  computed: {
    chartData() {
      return {
        labels: this.labels,
        datasets: [
          {
            label: this.label,
            data: this.data,
            backgroundColor: [
              "rgba(75, 192, 192, 1)", // color for the first bar
              "rgba(255, 99, 132, 1)", // color for the second bar
              "rgba(255, 159, 64, 1)", // color for the third bar
              "rgba(153, 102, 255, 1)", // color for the fourth bar
              "rgba(255, 205, 86, 1)", // color for the fifth bar
            ],
            borderColor: [
              "rgba(75, 192, 192, 1)", // color for the first bar
              "rgba(255, 99, 132, 1)", // color for the second bar
              "rgba(255, 159, 64, 1)", // color for the third bar
              "rgba(153, 102, 255, 1)", // color for the fourth bar
              "rgba(255, 205, 86, 1)", // color for the fifth bar
            ],
            borderWidth: 1,
          },
        ],
      };
    },
    chartOptions() {
      return {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: false,
            position: "top" as const,
          },
          title: {
            display: true,
            text: this.title,
          },
        },
      };
    },
  },
});
</script>
