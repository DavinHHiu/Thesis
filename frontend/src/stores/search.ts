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
    searchByImage(image: File, limit: number, offset: number) {
      const payload = {
        image,
      };
      return axios
        .post(`${consts.BASE_URL}/search/by-image/`, payload, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          console.log(response);
          return response;
        });
    },
    searchByText(keyword: String, limit: number, offset: number) {
      const payload = {
        text: keyword,
      };
      const params = {
        limit,
        offset,
      };
      return axios
        .post(`${consts.BASE_URL}/search/by-text/`, payload, { params })
        .then((response) => {
          console.log(response);
          return response;
        });
    },
  },
});
