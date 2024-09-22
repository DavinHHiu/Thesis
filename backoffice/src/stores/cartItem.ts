import consts from "@/consts/consts";
import { CartItem } from "@/types/worker";
import axios from "axios";
import _ from "lodash";
import { defineStore } from "pinia";

export const useCartItemStore = defineStore("cartItem", {
  state: () => {
    return {
      cartItem: {} as CartItem,
      cartItems: [] as CartItem[],
    };
  },
  actions: {
    createCartItem(payload: CartItem) {
      payload.product_sku = _.omit(payload.product_sku, ["images"]);
      return axios
        .post(`${consts.BASE_URL}/cart-items/`, payload)
        .then((response) => {
          console.log(response);
        });
    },
    listCartItems() {
      return axios.get(`${consts.BASE_URL}/cart-items/`).then((response) => {
        if (response.status === 200 && response.data) {
          this.cartItems = response.data.results;
        }
      });
    },
    retrieveCartItem(id: string) {
      return axios
        .get(`${consts.BASE_URL}/cart-items/${id}/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.cartItem = response.data;
          }
        });
    },
    updateCartItem(payload: CartItem) {
      payload.product_sku = _.omit(payload.product_sku, ["images"]);

      return axios
        .put(`${consts.BASE_URL}/cart-items/${payload.id}/`, payload)
        .then((response) => {
          console.log(response);
        });
    },
    destroyCartItem(id: number) {
      return axios
        .delete(`${consts.BASE_URL}/cart-items/${id}/`)
        .then((response) => {
          if (response.status === 204) {
            const updatedCartItems = _.filter(
              this.cartItems,
              (cartItem) => cartItem.id !== id
            );
            this.cartItems = updatedCartItems;
          }
        });
    },
    resetCartItem() {
      this.cartItem = {} as CartItem;
      this.cartItems = [] as CartItem[];
    },
  },
});
