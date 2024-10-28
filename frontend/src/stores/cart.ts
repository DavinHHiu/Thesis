import consts from "@/consts/consts";
import { Cart, CartItem, NewCartItem, User } from "@/types/worker";
import localStore from "@/utils/localStorage";
import axios from "axios";
import { defineStore } from "pinia";

export const useCartStore = defineStore("cart", {
  state: () => {
    return {
      cart: {} as Cart,
      cartItems: [] as CartItem[],
    };
  },
  actions: {
    retrieveCart() {
      const user = localStore.get("user") as User;
      if (user) {
        return axios
          .get(`${consts.BASE_URL}/carts/by-user/${user.id}/`)
          .then((response) => {
            if (response.status === 200 && response.data) {
              this.cart = response.data;
            }
          });
      }
    },
    addToCart(payload: NewCartItem) {
      return axios
        .post(`${consts.BASE_URL}/cart-items/`, payload)
        .then((response) => {
          if (response.status === 201 && response.data) {
            this.retrieveCart();
            this.listCartItems();
          }
        });
    },
    removeCartItem(id: number) {
      return axios
        .delete(`${consts.BASE_URL}/cart-items/${id}/`)
        .then((response) => {
          if (response.status === 204) {
            this.retrieveCart();
            this.listCartItems();
          }
        });
    },
    listCartItems() {
      return axios.get(`${consts.BASE_URL}/cart-items/`).then((response) => {
        if (response.status === 200 && response.data) {
          this.cartItems = response.data.results;
        }
      });
    },
    updateCartItemQuantity(cartItem: CartItem) {
      const payload = {
        cart_id: cartItem.cart_id,
        product_sku_id: cartItem.product_sku.id,
        quantity: cartItem.quantity,
      };
      return axios
        .put(`${consts.BASE_URL}/cart-items/${cartItem.id}/`, payload)
        .then((response) => {
          this.listCartItems();
          this.retrieveCart();
          return response;
        });
    },
  },
  getters: {
    totalQuantity: (state) => state.cart.total_quantity,
  },
});
