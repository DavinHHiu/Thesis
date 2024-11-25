import consts from "@/consts/consts";
import { Address, District, Province, Ward } from "@/types/worker";
import axios from "axios";
import { defineStore } from "pinia";

export const useAddressStore = defineStore("address", {
  state: () => {
    return {
      address: {} as Address,
      addresses: [] as Address[],
      province: {} as Province,
      district: {} as District,
      ward: {} as Ward,
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
    listProvinces() {
      return axios.get(`${consts.BASE_URL}/provinces/`).then((response) => {
        if (response.status === 200 && response.data) {
          return response;
        }
      });
    },
    listDistricts() {
      return axios.get(`${consts.BASE_URL}/districts/`).then((response) => {
        if (response.status === 200 && response.data) {
          return response;
        }
      });
    },
    listWards() {
      return axios
        .get(`${consts.BASE_URL}/wards/`, {
          params: {
            limit: 11000,
          },
        })
        .then((response) => {
          if (response.status === 200 && response.data) {
            return response;
          }
        });
    },
    listDistrictsByProvince(provinceCode: number) {
      return axios
        .get(`${consts.BASE_URL}/districts/by-province/${provinceCode}/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            return response;
          }
        });
    },
    listWardsByDistrict(districtCode: number) {
      return axios
        .get(`${consts.BASE_URL}/wards/by-district/${districtCode}/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            return response;
          }
        });
    },
    retrieveProvince(provinceCode: number) {
      return axios
        .get(`${consts.BASE_URL}/provinces/${provinceCode}/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.province = response.data;
          }
        });
    },
    retrieveDistrict(districtCode: number) {
      return axios
        .get(`${consts.BASE_URL}/districts/${districtCode}/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.district = response.data;
          }
        });
    },
    retrieveWard(wardCode: number) {
      return axios
        .get(`${consts.BASE_URL}/wards/${wardCode}/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.ward = response.data;
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
