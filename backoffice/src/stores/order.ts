import consts from "@/consts/consts";
import { Order } from "@/types/worker";
import axios from "axios";
import _ from "lodash";
import { defineStore } from "pinia";

export const useOrderStore = defineStore("order", {
  state: () => {
    return {
      order: {} as Order,
      orders: [] as Order[],
    };
  },
  actions: {
    createOrder(payload: Order) {
      payload.user = _.omit(payload.user, ["avatar", "password"]);
      return axios
        .post(`${consts.BASE_URL}/orders/`, payload)
        .then((response) => {
          console.log(response);
        });
    },
    listOrders() {
      return axios.get(`${consts.BASE_URL}/orders/`).then((response) => {
        if (response.status === 200 && response.data) {
          this.orders = response.data.results;
        }
      });
    },
    retrieveOrder(id: string) {
      return axios.get(`${consts.BASE_URL}/orders/${id}/`).then((response) => {
        if (response.status === 200 && response.data) {
          this.order = response.data;
        }
      });
    },
    updateOrder(payload: Order) {
      payload.user = _.omit(payload.user, ["avatar", "password"]);
      return axios
        .put(`${consts.BASE_URL}/orders/${payload.id}/`, payload)
        .then((response) => {
          console.log(response);
        });
    },
    destroyOrder(id: string) {
      return axios
        .delete(`${consts.BASE_URL}/orders/${id}/`)
        .then((response) => {
          if (response.status === 204) {
            const updatedOrders = _.filter(
              this.orders,
              (cart) => cart.id !== id
            );
            this.orders = updatedOrders;
          }
        });
    },
    resetOrder() {
      this.order = {} as Order;
      this.orders = [] as Order[];
    },
  },
});
