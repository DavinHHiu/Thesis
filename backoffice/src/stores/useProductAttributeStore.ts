import axios, { AxiosResponse } from "axios";

import { ProductAttribute } from "@/types/backoffice";
import { defineStore } from "pinia";

export const useProductAttributeStore = defineStore(
  "useProductAttributeStore",
  {
    actions: {
      async retrieveProductAttribute(id: number) {
        try {
          const response = await axios.get(
            `http://localhost:8000/api/v1/bo/product-attributes/${id}/`
          );
          return response;
        } catch (error: any) {
          alert(error.message);
        }
      },

      async listProductAttributes() {
        try {
          const response = await axios.get(
            "http://localhost:8000/api/v1/bo/product-attributes/"
          );
          return response;
        } catch (error: any) {
          alert(error.message);
        }
      },

      async createProductAttribute(params: ProductAttribute) {
        try {
          const response = await axios.post(
            "http://localhost:8000/api/v1/bo/product-attributes/",
            params
          );
          return response;
        } catch (error: any) {
          alert(error.message);
        }
      },

      async updateProductAttribute(params: ProductAttribute) {
        try {
          const response = await axios.put(
            `http://localhost:8000/api/v1/bo/product-attributes/${params.id}/`,
            params
          );
          return response;
        } catch (error: any) {
          alert(error.message);
        }
      },

      async destroyProductAttribute(id: number) {
        try {
          const response = await axios.delete(
            `http://localhost:8000/api/v1/bo/product-attributes/${id}/`
          );
          return response;
        } catch (error: any) {}
      },
    },
  }
);
