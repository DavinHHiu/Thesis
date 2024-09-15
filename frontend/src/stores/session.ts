import consts from "@/consts/consts";
import { LoginItem, RegisterItem } from "@/types/frontend";
import { User } from "@/types/worker";
import localStore from "@/utils/localStorage";
import axios from "axios";
import { defineStore } from "pinia";

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
            this.token = "keep";
            this.user = response.data.user;
            if (response.data.token) {
              axios.defaults.headers.common["Authorization"] =
                `Bearer ${response.data.token}`;
            }
            localStore.bulkSet({
              token: response.data.token,
              user: JSON.stringify(this.user),
            });

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
      return axios.post(`${consts.BASE_URL}/register/`, payload);
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
      const payload = {
        token: localStore.get("token"),
      };
      return axios
        .post(`${consts.BASE_URL}/token/refresh/`, payload)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.token = "keep";
            this.user = response.data.user;
            if (response.data.token) {
              axios.defaults.headers.common["Authorization"] =
                `Bearer ${response.data.token}`;
            }
          }
        });
    },
  },
  getters: {
    isAuthenticated: (state) => {
      return !!localStore.get("token");
    },
  },
});
