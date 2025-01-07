import consts from "@/consts/consts";
import { ProductAttribute } from "@/types/worker";
import axios from "axios";
import { defineStore } from "pinia";

export const useProductAttributeStore = defineStore("productAttribute", {
  state: () => {
    return {
      productAttribute: {} as ProductAttribute,
      productAttributes: [] as ProductAttribute[],
    };
  },
  actions: {
    retrieveProductAttribute(id: number) {
      return axios
        .get(`${consts.BASE_URL}/product-attributes/${id}/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.productAttribute = response.data;
          }
        });
    },
    listProductAttributes(params: Object) {
      return axios
        .get(`${consts.BASE_URL}/product-attributes/`, { params })
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.productAttributes = response.data.results;
            return response;
          }
        });
    },
    createProductAttribute(payload: ProductAttribute) {
      return axios
        .post(`${consts.BASE_URL}/product-attributes/`, payload)
        .then((response) => response);
    },
    updateProductAttribute(payload: ProductAttribute) {
      return axios
        .put(`${consts.BASE_URL}/product-attributes/${payload.id}/`, payload)
        .then((response) => response);
    },
    destroyProductAttribute(id: number) {
      return axios
        .delete(`${consts.BASE_URL}/product-attributes/${id}/`)
        .then((response) => {
          if (response.status === 204) {
            const updatedProductAttributes = this.productAttributes.filter(
              (productAttribute: ProductAttribute) => productAttribute.id !== id
            );
            this.productAttributes = updatedProductAttributes;
          }
        });
    },
    resetProductAttribute() {
      this.productAttribute = {} as ProductAttribute;
      this.productAttributes = [] as ProductAttribute[];
    },
  },
});
