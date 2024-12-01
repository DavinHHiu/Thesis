import consts from "@/consts/consts";
import { Category } from "@/types/worker";
import axios from "axios";
import _ from "lodash";
import { defineStore } from "pinia";

export const useCategoryStore = defineStore("category", {
  state: () => {
    return {
      category: {} as Category,
      categories: [] as Category[],
    };
  },
  actions: {
    createCategory(payload: Category) {
      return axios
        .post(`${consts.BASE_URL}/categories/`, payload)
        .then((response) => response);
    },
    listCategories() {
      return axios.get(`${consts.BASE_URL}/categories/`).then((response) => {
        if (response.status === 200 && response.data) {
          this.categories = response.data.results;
        }
      });
    },
    retrieveCategory(id: number) {
      return axios
        .get(`${consts.BASE_URL}/categories/${id}/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.category = response.data;
          }
        });
    },
    updateCategory(payload: Category) {
      return axios
        .put(`${consts.BASE_URL}/categories/${payload.id}/`, payload)
        .then((response) => response);
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
    resetCategory() {
      this.category = {} as Category;
      this.categories = [] as Category[];
    },
  },
});
