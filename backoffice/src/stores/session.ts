import { LoginItem } from "@/types/backoffice";
import { User } from "@/types/worker";
import axios from "axios";
import consts from "@/consts/consts";
import { defineStore } from "pinia";
import localStore from "@/utils/localStorage";

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
            localStore.set("token", this.token);

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
    logout() {
      this.resetSession();
      localStore.remove("token");
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
    resetSession() {
      this.user = {} as User;
      this.token = "";
    },
  },
  getters: {
    isAuthenticated: (state) => {
      return !!localStore.get("token");
    },
  },
});
