import consts from "@/consts/consts";
import { Category } from "@/types/worker";
import axios from "axios";
import _ from "lodash";
import { defineStore } from "pinia";

export const useCategoryStore = defineStore("category", {
  state: () => {
    return {
      currentCategory: {} as Category,
      categories: [] as Category[],
    };
  },
  actions: {
    retrieveCategory(id: number) {
      return axios
        .get(`${consts.BASE_URL}/categories/${id}/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.currentCategory = response.data;
          }
        });
    },
    listCategories() {
      return axios.get(`${consts.BASE_URL}/categories/`).then((response) => {
        if (response.status === 200 && response.data) {
          this.categories = response.data.results;
        }
      });
    },
    createCategory(payload: Category) {
      return axios
        .post(`${consts.BASE_URL}/categories/`, payload)
        .then((response) => {
          console.log(response);
        });
    },
    destroyCategory(id: number) {
      return axios
        .delete(`${consts.BASE_URL}/categories/${id}/`)
        .then((response) => {
          if (response.status === 204) {
            const updatedCategories = _.filter(
              this.categories,
              (category: Category) => category.id !== id
            );
            this.categories = updatedCategories;
          }
        });
    },
    update(payload: Category) {
      return axios
        .put(`${consts.BASE_URL}/categories/${payload.id}/`, payload)
        .then((response) => {
          console.log(response);
        });
    },
  },
});
