import consts from "@/consts/consts";
import { Product, ProductDetail } from "@/types/worker";
import axios from "axios";
import _ from "lodash";
import { defineStore } from "pinia";

export const useProductStore = defineStore("product", {
  state: () => {
    return {
      productDetail: {} as ProductDetail,
      products: [] as Product[],
    };
  },
  actions: {
    listProducts(params?: object) {
      return axios
        .get(`${consts.BASE_URL}/products/`, {
          params: params,
        })
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.products = response.data;
          }
        });
    },
    retrieveProductDetail(id: string) {
      return axios
        .get(`${consts.BASE_URL}/products/${id}/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.productDetail = response.data;
          }
        });
    },
    resetProduct() {
      this.productDetail = {} as ProductDetail;
      this.products = [] as Product[];
    },
  },
});
