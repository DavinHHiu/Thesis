import consts from "@/consts/consts";
import { AuthToken, LoginItem } from "@/types/backoffice";
import axios from "axios";
import { jwtDecode } from "jwt-decode";
import { defineStore } from "pinia";
import { useRouter } from "vue-router";

let refreshInterval: NodeJS.Timeout | null = null;

export const useAuthStore = defineStore("auth", {
  state: () => {
    return {
      isAuthenticated: false,
      user: {},
      authTokens: {} as AuthToken,
    };
  },
  actions: {
    login(payload: LoginItem) {
      return axios
        .post(`${consts.APP_URL}/token/`, payload)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.authTokens = response.data;
            this.user = jwtDecode(this.authTokens.access);
            this.isAuthenticated = true;
            localStorage.setItem("authTokens", JSON.stringify(this.authTokens));

            refreshInterval = setInterval(
              () => {
                if (this.isAuthenticated) {
                  this.updateToken();
                }
              },
              4 * 60 * 1000
            );
          } else {
            alert("Something went wrong!");
          }
        });
    },
    logout() {
      this.authTokens = {} as AuthToken;
      this.user = {};
      this.isAuthenticated = false;
      localStorage.removeItem("authTokens");

      if (refreshInterval) {
        clearInterval(refreshInterval);
        refreshInterval = null;
      }
    },
    updateToken() {
      const payload = {
        refresh: this.authTokens.refresh,
      };
      return axios
        .post(`${consts.APP_URL}/token/refresh/`, payload)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.authTokens = response.data;
            this.user = jwtDecode(this.authTokens.access);
            this.isAuthenticated = true;
            localStorage.setItem("authTokens", JSON.stringify(this.authTokens));
          } else {
            this.logout();
          }
        });
    },
  },
});
