import consts from "@/consts/consts";
import { ShipmentMethod } from "@/types/worker";
import axios from "axios";
import { defineStore } from "pinia";

export const useShipmentStore = defineStore("shipment", {
  state: () => {
    return {
      shipmentMethod: {} as ShipmentMethod,
      shipmentMethods: [] as ShipmentMethod[],
    };
  },
  actions: {
    listShipmentMethods() {
      return axios
        .get(`${consts.BASE_URL}/shipment-methods/`)
        .then((response) => {
          if (response.status === 200 && response.data) {
            this.shipmentMethods = response.data.results;
          }
        });
    },
    setShipmentMethod(method: ShipmentMethod) {
      this.shipmentMethod = method;
    },
  },
});
