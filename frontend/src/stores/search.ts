import consts from "@/consts/consts";
import axios from "axios";
import { defineStore } from "pinia";

export const useSearchStore = defineStore("search", {
  state() {
    return {
      query: "",
    };
  },
  actions: {
    searchByImage(payload: Object, params: Object) {
      return axios
        .post(`${consts.BASE_URL}/search/by-image/`, payload, { params })
        .then((response) => {
          console.log(response);
          return response;
        });
    },
    searchByText(payload: Object, params: Object) {
      return axios
        .post(`${consts.BASE_URL}/search/by-text/`, payload, { params })
        .then((response) => {
          console.log(response);
          return response;
        });
    },
  },
});
