import consts from "@/consts/consts";
import { User } from "@/types/worker";
import axios from "axios";
import _ from "lodash";
import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
  state: () => {
    return {
      user: {} as User,
      users: [] as User[],
    };
  },
  actions: {
    createUser(payload: User) {
      return axios
        .post(`${consts.BASE_URL}/users/`, payload, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => response);
    },
    listUsers(params: Object) {
      return axios
        .get(`${consts.BASE_URL}/users/`, { params })
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.users = response.data.results;
            return response;
          }
        });
    },
    retrieveUser(id: string) {
      return axios.get(`${consts.BASE_URL}/users/${id}/`).then((response) => {
        if (response.status === 200 && response.data) {
          this.user = response.data;
        }
      });
    },
    updateUser(payload: User) {
      if (payload.avatar && !(payload.avatar instanceof File)) {
        payload = _.omit(payload, ["avatar"]);
      }
      return axios
        .put(`${consts.BASE_URL}/users/${payload.id}/`, payload, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => response);
    },
    destroyUser(id: string) {
      return axios
        .delete(`${consts.BASE_URL}/users/${id}/`)
        .then((response) => {
          if (response.status === 204) {
            const updatedUsers = this.users.filter(
              (user: User) => user.id !== id
            );
            this.users = updatedUsers;
          }
        });
    },
    resetUser() {
      this.user = {} as User;
      this.users = [] as User[];
    },
  },
});
