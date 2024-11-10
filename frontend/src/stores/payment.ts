import consts from "@/consts/consts";
import { PaymentMethod } from "@/types/worker";
import axios from "axios";
import { defineStore } from "pinia";

export const usePaymentStore = defineStore("payment", {
  state: () => {
    return {
      paymentMethods: [] as PaymentMethod[],
    };
  },
  actions: {
    listPaymentMethods() {
      return axios
        .get(`${consts.BASE_URL}/payment-methods/`)
        .then((response) => {
          this.paymentMethods = response.data.results;
        });
    },
  },
});
