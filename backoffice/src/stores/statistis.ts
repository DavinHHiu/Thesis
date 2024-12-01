import consts from "@/consts/consts";
import { Period } from "@/types/backoffice";
import axios from "axios";
import { defineStore } from "pinia";

export const useStatistic = defineStore("statistic", {
  state() {
    return {};
  },
  actions: {
    fetchRevenueStatistic(period: Period) {
      return axios
        .post(`${consts.BASE_URL}/revenue-statistics/`, {
          ...period,
        })
        .then((response) => response);
    },
  },
});
