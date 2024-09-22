import consts from "@/consts/consts";
import { Address } from "@/types/worker";
import axios from "axios";
import _ from "lodash";
import { defineStore } from "pinia";

export const useAddressStore = defineStore("address", {
  state: () => {
    return {
      address: {} as Address,
      addresses: [] as Address[],
    };
  },
  actions: {
    createAddress(payload: Address) {
      payload.user = _.omit(payload.user, ["avatar", "password"]);
      return axios
        .post(`${consts.BASE_URL}/addresses/`, payload)
        .then((response) => {
          console.log(response);
        });
    },
    listAddresses() {
      return axios.get(`${consts.BASE_URL}/addresses/`).then((response) => {
        if (response.status === 200 && response.data) {
          this.addresses = response.data.results;
        }
      });
    },
    retrieveAddress(id: number) {
      return axios
        .get(`${consts.BASE_URL}/addresses/${id}/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.address = response.data;
          }
        });
    },
    updateAddress(payload: Address) {
      payload.user = _.omit(payload.user, ["avatar", "password"]);
      return axios
        .put(`${consts.BASE_URL}/addresses/${payload.id}/`, payload)
        .then((response) => {
          console.log(response);
        });
    },
    destroyAddress(id: number) {
      return axios
        .delete(`${consts.BASE_URL}/addresses/${id}/`)
        .then((response) => {
          if (response.status === 204) {
            const updatedAddresses = _.filter(
              this.addresses,
              (address) => address.id !== id
            );
            this.addresses = updatedAddresses;
          }
        });
    },
    resetAddress() {
      this.address = {} as Address;
      this.addresses = [] as Address[];
    },
  },
});
