import consts from "@/consts/consts";
import { Product } from "@/types/worker";
import axios from "axios";
import _ from "lodash";
import { defineStore } from "pinia";

export const useProductStore = defineStore("product", {
  state: () => {
    return {
      product: {} as Product,
      products: [] as Product[],
    };
  },
  actions: {
    createProduct(payload: Product) {
      return axios
        .post(`${consts.BASE_URL}/products/`, payload)
        .then((response) => {
          console.log(response);
        });
    },
    listProducts() {
      return axios.get(`${consts.BASE_URL}/products/`).then((response) => {
        if (response.status === 200 && response.data) {
          this.products = response.data.results;
        }
      });
    },
    retrieveProduct(id: string) {
      return axios
        .get(`${consts.BASE_URL}/products/${id}/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.product = response.data;
          }
        });
    },
    updateProduct(payload: Product) {
      return axios
        .put(`${consts.BASE_URL}/products/${payload.id}/`, payload)
        .then((response) => {
          console.log(response);
        });
    },
    destroyProduct(id: string) {
      return axios
        .delete(`${consts.BASE_URL}/products/${id}/`)
        .then((response) => {
          if (response.status === 204) {
            const updatedProducts = _.filter(
              this.products,
              (product) => product.id !== id
            );
            this.products = updatedProducts;
          }
        });
    },
  },
});
