import consts from "@/consts/consts";
import { Category } from "@/types/worker";
import axios from "axios";
import { defineStore } from "pinia";

export const useCategoryStore = defineStore("category", {
  state() {
    return {
      categories: [] as Category[],
    };
  },
  actions: {
    listCategories() {
      return axios.get(`${consts.BASE_URL}/categories/`).then((response) => {
        if (response.status === 200 && response.data) {
          this.categories = response.data.results;
        }
      });
    },
    listSubCategoryByCategory(categoryId: number) {
      return axios
        .get(`${consts.BASE_URL}/subcategories/by-category/`, {
          params: {
            category_id: categoryId,
          },
        })
        .then((response) => response);
    },
  },
});
