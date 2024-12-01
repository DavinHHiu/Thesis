import consts from "@/consts/consts";
import { SubCategory } from "@/types/worker";
import axios from "axios";
import { defineStore } from "pinia";

export const useSubCategoryStore = defineStore("subcategory", {
  state: () => {
    return {
      subcategory: {} as SubCategory,
      subcategories: [] as SubCategory[],
    };
  },
  actions: {
    createSubCategory(payload: SubCategory) {
      return axios
        .post(`${consts.BASE_URL}/sub-categories/`, payload)
        .then((response) => {
          if (response.status === 201 && response.data) {
          }
        });
    },
    listSubCategories() {
      return axios
        .get(`${consts.BASE_URL}/sub-categories/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.subcategories = response.data.results;
          }
        });
    },
    listByCategory(category_id: number) {
      return axios
        .get(`${consts.BASE_URL}/sub-categories/by-category/`, {
          params: {
            category_id: category_id,
          },
        })
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.subcategories = response.data;
          }
        });
    },
    retrieveSubCategory(id: number) {
      return axios
        .get(`${consts.BASE_URL}/sub-categories/${id}/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.subcategory = response.data;
          }
        });
    },
    updateSubCategory(payload: SubCategory) {
      return axios
        .put(`${consts.BASE_URL}/sub-categories/${payload.id}/`, payload)
        .then((response) => response);
    },
    destroySubCategory(id: number) {
      return axios
        .delete(`${consts.BASE_URL}/sub-categories/${id}/`)
        .then((response) => {
          if (response.status === 204) {
            const updatedSubcategories = this.subcategories.filter(
              (subcategory: SubCategory) => subcategory.id !== id
            );
            this.subcategories = updatedSubcategories;
          }
        });
    },
    resetSubCategory() {
      this.subcategory = {} as SubCategory;
      this.subcategories = [] as SubCategory[];
    },
  },
});
