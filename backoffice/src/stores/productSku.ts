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
        .post(`${consts.BASE_URL}/product-skus/`, payload)
        .then((response) => {
          if (response.status === 201 && response.data) {
            const formData = new FormData();
            _.forEach(payload.images, (image) => {
              formData.append("images", image);
            });
            formData.append("product_sku_id", response.data.id);

            axios
              .post(`${consts.BASE_URL}/product-images/`, formData, {
                headers: {
                  "Content-Type": "multipart/form-data",
                },
              })
              .then((response) => {
                console.log(response);
              });
          }
        });
    },
    listProductSkus(product_id: string) {
      return axios
        .get(`${consts.BASE_URL}/product-skus/`, {
          params: {
            product_id: product_id,
          },
        })
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.productSkus = response.data;
          }
        });
    },
    retrieveProductSku(id: string) {
      return axios
        .get(`${consts.BASE_URL}/product-skus/${id}/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.productSku = response.data;
            axios
              .get(`${consts.BASE_URL}/product-images/`, {
                params: { product_sku_id: this.productSku.id },
              })
              .then((res) => {
                if (res.status === 200 && res.data) {
                  const images = _.map(res.data, "image");
                  this.productSku.images = images;
                }
              });
          }
        });
    },
    updateProductSku(payload: ProductSku) {
      return axios
        .put(`${consts.BASE_URL}/product-skus/${payload.id}/`, payload)
        .then((response) => {
          if (response.status === 200 && response.data) {
            const formData = new FormData();
            _.forEach(payload.images, (image) => {
              formData.append("images", image);
            });
            formData.append("product_sku_id", response.data.id);

            axios
              .post(`${consts.BASE_URL}/product-images/`, formData, {
                headers: {
                  "Content-Type": "multipart/form-data",
                },
              })
              .then((response) => {
                console.log(response);
              });
          }
        });
    },
    destroyProductSku(id: string) {
      return axios
        .delete(`${consts.BASE_URL}/product-skus/${id}/`)
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
    resetProductSku() {
      this.productSku = {} as ProductSku;
      this.productSkus = [] as ProductSku[];
    },
  },
});
