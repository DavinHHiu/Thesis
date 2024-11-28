import consts from "@/consts/consts";
import { Address, District, Province, Ward } from "@/types/worker";
import axios from "axios";
import _ from "lodash";
import { defineStore } from "pinia";

export const useAddressStore = defineStore("address", {
  state: () => {
    return {
      address: {} as Address,
      addresses: [] as Address[],
      province: {} as Province,
      provinces: [] as Province[],
      district: {} as District,
      districts: [] as District[],
      ward: {} as Ward,
      wards: [] as Ward[],
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
    listProvinces() {
      return axios.get(`${consts.BASE_URL}/provinces/`).then((response) => {
        if (response.status === 200 && response.data) {
          this.provinces = response.data.results;
        }
      });
    },
    listDistricts() {
      return axios.get(`${consts.BASE_URL}/districts/`).then((response) => {
        if (response.status === 200 && response.data) {
          this.districts = response.data.results;
        }
      });
    },
    listWards() {
      return axios.get(`${consts.BASE_URL}/wards/`).then((response) => {
        if (response.status === 200 && response.data) {
          this.wards = response.data.results;
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
    resetAddress() {
      this.address = {} as Address;
      this.addresses = [] as Address[];
    },
  },
});
