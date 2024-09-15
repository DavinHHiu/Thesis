import consts from "@/consts/consts";
import { ProductSku } from "@/types/worker";
import axios from "axios";
import _ from "lodash";
import { defineStore } from "pinia";

export const useProductSkuStore = defineStore("productSku", {
  state: () => {
    return {
      productSku: {} as ProductSku,
      productSkus: [] as ProductSku[],
    };
  },
  actions: {
    createProductSku(payload: ProductSku) {
      return axios
        .post(`${consts.BASE_URL}/products/`, payload, {
          headers: {
            "Content-type": "multipart/form-data",
          },
        })
        .then((response) => {
          console.log(response);
        });
    },
    listProductSkus() {
      return axios.get(`${consts.BASE_URL}/products/`).then((response) => {
        if (response.status === 200 && response.data) {
          this.productSkus = response.data;
        }
      });
    },
    retrieveProductSku(id: string) {
      return axios
        .get(`${consts.BASE_URL}/products/${id}/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.productSku = response.data;
          }
        });
    },
    updateProductSku(payload: ProductSku) {
      if (typeof payload.cover === "string") {
        payload = _.omit(payload, ["cover"]);
      }
      return axios
        .put(`${consts.BASE_URL}/products/${payload.id}/`, payload, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          console.log(response);
        });
    },
    destroyProductSku(id: string) {
      return axios
        .delete(`${consts.BASE_URL}/products/${id}/`)
        .then((response) => {
          if (response.status === 204) {
            const updatedProducts = _.filter(
              this.productSkus,
              (product) => product.id !== id
            );
            this.productSkus = updatedProducts;
          }
        });
    },
  },
});
