import consts from "@/consts/consts";
import { OrderItem } from "@/types/worker";
import axios from "axios";
import _ from "lodash";
import { defineStore } from "pinia";

export const useOrderItemStore = defineStore("orderItem", {
  state: () => {
    return {
      orderItem: {} as OrderItem,
      orderItems: [] as OrderItem[],
    };
  },
  actions: {
    createOrderItem(payload: OrderItem) {
      payload.product_sku = _.omit(payload.product_sku, ["images"]);
      return axios
        .post(`${consts.BASE_URL}/order-items/`, payload)
        .then((response) => {
          console.log(response);
        });
    },
    listOrderItems() {
      return axios.get(`${consts.BASE_URL}/order-items/`).then((response) => {
        if (response.status === 200 && response.data) {
          this.orderItems = response.data.results;
        }
      });
    },
    retrieveOrderItem(id: string) {
      return axios
        .get(`${consts.BASE_URL}/order-items/${id}/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.orderItem = response.data;
          }
        });
    },
    updateOrderItem(payload: OrderItem) {
      payload.product_sku = _.omit(payload.product_sku, ["images"]);

      return axios
        .put(`${consts.BASE_URL}/order-items/${payload.id}/`, payload)
        .then((response) => {
          console.log(response);
        });
    },
    destroyOrderItem(id: string) {
      return axios
        .delete(`${consts.BASE_URL}/order-items/${id}/`)
        .then((response) => {
          if (response.status === 204) {
            const updatedOrderItems = _.filter(
              this.orderItems,
              (orderItem) => orderItem.id !== id
            );
            this.orderItems = updatedOrderItems;
          }
        });
    },
    resetOrderItem() {
      this.orderItem = {} as OrderItem;
      this.orderItems = [] as OrderItem[];
    },
  },
});
