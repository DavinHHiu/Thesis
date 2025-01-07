import { CartItem, Order, OrderItem, User } from "@/types/worker";

import axios from "axios";
import consts from "@/consts/consts";
import { defineStore } from "pinia";

export const useOrderStore = defineStore("order", {
  state: () => {
    return {
      order: {} as Order,
      orders: [] as Order[],
      orderItems: [] as OrderItem[],
    };
  },
  actions: {
    createOrderItems(
      checkoutItems: CartItem[],
      totalAmount: number,
      orderId: string
    ) {
      const payload = {
        checkout_items: checkoutItems,
        total_amount: totalAmount,
        order_id: orderId,
      };
      return axios
        .post(`${consts.BASE_URL}/order-items/`, payload)
        .then((response) => {});
    },
    executePayment(token: string, PayerID: string, paymentId: string) {
      return axios
        .post(`${consts.BASE_URL}/execute-payment/`, {
          token,
          PayerID,
          paymentId,
        })
        .then((response) => {
          return response;
        });
    },
    retrieveOrder(orderId: string) {
      return axios
        .get(`${consts.BASE_URL}/orders/${orderId}/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.order = response.data;
          }
        });
    },
    listOrderItems(orderId: string) {
      return axios
        .get(`${consts.BASE_URL}/order-items/by-order/${orderId}/`)
        .then((response) => {
          this.orderItems = response.data;
        });
    },
    listOrders(params: Object) {
      return axios
        .get(`${consts.BASE_URL}/orders/`, {
          params,
        })
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.orders = response.data.results;
          }
          return response;
        });
    },
  },
});
