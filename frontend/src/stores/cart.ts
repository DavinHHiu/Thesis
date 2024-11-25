import consts from "@/consts/consts";
import { useOrderStore } from "@/stores/order";
import {
  Address,
  Cart,
  CartItem,
  NewCartItem,
  PaymentMethod,
  ShipmentMethod,
} from "@/types/worker";
import axios from "axios";
import { defineStore } from "pinia";

export const useCartStore = defineStore("cart", {
  state: () => {
    return {
      cart: {} as Cart,
      cartItems: [] as CartItem[],
      checkoutItems: [] as CartItem[],
    };
  },
  actions: {
    retrieveCart() {
      return axios.get(`${consts.BASE_URL}/carts/by-user/`).then((response) => {
        if (response.status === 200 && response.data) {
          this.cart = response.data;
          console.log(this.cart);
        }
      });
    },
    addToCart(payload: NewCartItem) {
      return axios
        .post(`${consts.BASE_URL}/cart-items/`, payload)
        .then(async (response) => {
          if (response.status === 201 && response.data) {
            await this.retrieveCart();
            await this.listCartItems();
          }
          return response;
        });
    },
    removeCartItem(id: number) {
      return axios
        .delete(`${consts.BASE_URL}/cart-items/${id}/`)
        .then(async (response) => {
          if (response.status === 204) {
            await this.retrieveCart();
            await this.listCartItems();
          }
          return response;
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
    validateCheckoutItems() {
      const payload = {
        checkout_items: this.checkoutItems,
      };
      return axios
        .post(`${consts.BASE_URL}/cart-items/validate/checkout-items/`, payload)
        .then((response) => {
          this.checkoutItems = response.data;
          return response;
        });
    },
    createPayment(
      totalAmount: number,
      totalQuantity: number,
      address: Address,
      shipmentMethod: ShipmentMethod,
      paymentMethod: PaymentMethod
    ) {
      const host = window.location.origin;
      const payload = {
        total_amount: totalAmount,
        total_quantity: totalQuantity,
        host: host,
        address: address,
        shipment_method: shipmentMethod,
        payment_method: paymentMethod,
      };
      return axios
        .post(`${consts.BASE_URL}/create-payment/`, payload)
        .then((response) => {
          const orderStore = useOrderStore();
          const orderId = response.data.order_id;
          orderStore.createOrderItems(this.checkoutItems, totalAmount, orderId);
          if (response.data.approval_url) {
            window.location.href = response.data.approval_url;
          }
          return response;
        });
    },
    setCheckoutItems(items: CartItem[]) {
      this.checkoutItems = items;
    },
  },
  getters: {
    totalQuantity: (state) => state.cart.total_quantity,
  },
});
