import consts from "@/consts/consts";
import { LoginItem, RegisterItem } from "@/types/frontend";
import { Password, User } from "@/types/worker";
import localStore from "@/utils/localStorage";
import axios from "axios";
import _ from "lodash";
import { defineStore } from "pinia";

import { useCartStore } from "./cart";

let refreshInterval: NodeJS.Timeout | null = null;

export const useSessionStore = defineStore("session", {
  state: () => {
    return {
      user: {} as User,
      token: "",
    };
  },
  actions: {
    login(payload: LoginItem) {
      return axios
        .post(`${consts.BASE_URL}/token/`, payload)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.token = response.data.token;
            this.user = response.data.user;
            if (response.data.token) {
              axios.defaults.headers.common["Authorization"] =
                `Bearer ${this.token}`;
            }
            localStore.bulkSet({
              token: this.token,
              user: JSON.stringify(this.user),
            });

            if (this.user.id) {
              const cartStore = useCartStore();
              cartStore.retrieveCart();
            }

            refreshInterval = setInterval(
              () => {
                if (this.isAuthenticated) {
                  this.refresh();
                }
              },
              4 * 60 * 1000
            );

            return response;
          } else {
            alert("Something went wrong!");
          }
        });
    },
    register(payload: RegisterItem) {
      return axios
        .post(`${consts.BASE_URL}/register/`, payload)
        .then((response) => response);
    },
    logout() {
      this.token = "";
      this.user = {} as User;
      localStore.bulkRemove(["user", "token"]);
      delete axios.defaults.headers.common["Authorization"];

      if (refreshInterval) {
        clearInterval(refreshInterval);
        refreshInterval = null;
      }
    },
    refresh() {
      const requestToken = localStore.get("token");
      if (requestToken) {
        const payload = {
          token: requestToken,
        };
        return axios
          .post(`${consts.BASE_URL}/token/refresh/`, payload)
          .then((response) => {
            if (response.status === 200 && response.data) {
              this.token = response.data.token;
              this.user = response.data.user;
              if (response.data.token) {
                axios.defaults.headers.common["Authorization"] =
                  `Bearer ${response.data.token}`;
              }
            }
          });
      }
    },
    updateUser(payload: User) {
      payload = _.omit(payload, ["avatar"]);
      return axios
        .put(`${consts.BASE_URL}/users/${payload.id}/`, payload)
        .then((response) => {
          return response;
        });
    },
    resetPassword(payload: Password) {
      return axios
        .post(`${consts.BASE_URL}/change-password/`, payload)
        .then((response) => {
          return response;
        });
    },
  },
  getters: {
    isAuthenticated: (state) => {
      return !!state.token;
    },
  },
});
