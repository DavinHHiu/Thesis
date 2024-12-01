import consts from "@/consts/consts";
import { Cart } from "@/types/worker";
import axios from "axios";
import _ from "lodash";
import { defineStore } from "pinia";

export const useCartStore = defineStore("cart", {
  state: () => {
    return {
      cart: {} as Cart,
      carts: [] as Cart[],
    };
  },
  actions: {
    createCart(payload: Cart) {
      payload.user = _.omit(payload.user, ["avatar", "password"]);
      return axios
        .post(`${consts.BASE_URL}/carts/`, payload)
        .then((response) => response);
    },
    listCarts() {
      return axios.get(`${consts.BASE_URL}/carts/`).then((response) => {
        if (response.status === 200 && response.data) {
          this.carts = response.data.results;
        }
      });
    },
    retrieveCart(id: string) {
      return axios.get(`${consts.BASE_URL}/carts/${id}/`).then((response) => {
        if (response.status === 200 && response.data) {
          this.cart = response.data;
        }
      });
    },
    updateCart(payload: Cart) {
      payload.user = _.omit(payload.user, ["avatar", "password"]);
      return axios
        .put(`${consts.BASE_URL}/carts/${payload.id}/`, payload)
        .then((response) => response);
    },
    destroyCart(id: string) {
      return axios
        .delete(`${consts.BASE_URL}/carts/${id}/`)
        .then((response) => {
          if (response.status === 204) {
            const updatedCarts = _.filter(this.carts, (cart) => cart.id !== id);
            this.carts = updatedCarts;
          }
        });
    },
    resetCart() {
      this.cart = {} as Cart;
      this.carts = [] as Cart[];
    },
  },
});
