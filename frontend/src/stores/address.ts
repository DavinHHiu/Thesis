import consts from "@/consts/consts";
import { Address } from "@/types/worker";
import localStore from "@/utils/localStorage";
import axios from "axios";
import { defineStore } from "pinia";

export const useAddressStore = defineStore("address", {
  state: () => {
    return {
      address: {} as Address,
      addresses: [] as Address[],
    };
  },
  actions: {
    async createAddress(payload: Address) {
      return axios
        .post(`${consts.BASE_URL}/addresses/`, payload)
        .then(async (response) => {
          if (response.status === 201 && response.data) {
            await this.listAddressesByUser();
            return response;
          }
        });
    },
    async updateAddress(payload: Address) {
      return axios
        .put(`${consts.BASE_URL}/addresses/${payload.id}/`, payload)
        .then(async (response) => {
          if (response.status === 200 && response.data) {
            await this.listAddressesByUser();
            return response;
          }
        });
    },
    listAddressesByUser() {
      return axios
        .get(`${consts.BASE_URL}/addresses/by-user/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.addresses = response.data;
          }
        });
    },
    async destroyAddress(address: Address) {
      return axios
        .delete(`${consts.BASE_URL}/addresses/${address.id}/`)
        .then(async (response) => {
          await this.listAddressesByUser();
          return response;
        });
    },
    setAddress(addr: Address) {
      this.address = addr;
    },
  },
});
