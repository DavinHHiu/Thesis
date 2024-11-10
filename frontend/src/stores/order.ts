import consts from "@/consts/consts";
import { CartItem, Order, OrderItem, User } from "@/types/worker";
import localStore from "@/utils/localStorage";
import axios from "axios";
import { defineStore } from "pinia";

export const useOrderStore = defineStore("order", {
  state: () => {
    return {
      order: {} as Order,
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
    executePayment(token: string, PayerID: string) {
      return axios
        .post(`${consts.BASE_URL}/execute-payment/`, {
          token,
          PayerID,
        })
        .then((response) => {
          return response;
        });
    },
    retrieveOrder(orderId: string) {
      return axios
        .get(`${consts.BASE_URL}/order/${orderId}/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.order = response.data;
            console.log(response);
          }
        });
    },
    retrieveOrderItems(orderId: string) {
      return axios
        .get(`${consts.BASE_URL}/order-items/by-order/${orderId}/`)
        .then((response) => {
          this.orderItems = response.data;
        });
    },
  },
});
