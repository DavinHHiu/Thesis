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
    listProductAttributes() {
      return axios
        .get(`${consts.BASE_URL}/product-attributes/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.productAttributes = response.data;
          }
        });
    },
    createProductAttribute(payload: ProductAttribute) {
      return axios
        .post(`${consts.BASE_URL}/product-attributes/`, payload)
        .then((response) => {
          console.log(response);
        });
    },
    updateProductAttribute(payload: ProductAttribute) {
      return axios
        .put(`${consts.BASE_URL}/product-attributes/${payload.id}/`, payload)
        .then((response) => {
          console.log(response);
        });
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
  },
});
