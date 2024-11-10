<template>
  <div class="wrapper">
    <label
      v-for="(method, index) in shipmentMethods"
      class="shipment-method-item"
      :class="{ active: index === curIdx }"
    >
      <input
        type="radio"
        name="shipment-method"
        :checked="index === curIdx"
        @click="changeIndex(index)"
      />
      <div class="info-wrapper">
        <div class="info">
          <span>
            <span class="method-name" v-text="method.name" />
            <span
              class="method-estimated-date"
              v-text="` - ${method.estimated_shipping_days} days`"
            />
          </span>
          <span class="method-description" v-text="method.description" />
        </div>
        <span class="shipment-fee" v-text="`$${method.shipping_fee}.00`" />
      </div>
    </label>
  </div>
</template>

<script lang="ts">
import { useShipmentStore } from "@/stores/shipment";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "ShipmentSelect",
  emits: ["update:shipmentMethod"],
  data() {
    return {
      curIdx: 0,
    };
  },
  computed: {
    ...mapState(useShipmentStore, ["shipmentMethods"]),
  },
  methods: {
    ...mapActions(useShipmentStore, ["listShipmentMethods"]),
    changeIndex(index: number) {
      this.curIdx = index;
      this.$emit("update:shipmentMethod", index);
    },
  },
  async mounted() {
    await this.listShipmentMethods();
    this.$emit("update:shipmentMethod", this.curIdx);
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.wrapper {
  display: flex;
  flex-direction: column;
  gap: 1rem;

  .shipment-method-item {
    display: flex;
    gap: 2rem;
    padding: 2rem;
    border-radius: 0.4rem;
    border: 1px solid $--color-border;
    color: $--gray-color-900;
    transition: 0.25s ease-in-out;
    user-select: none;
    cursor: pointer;

    &.active {
      border: 1px solid $--primary-color;
    }

    &:active {
      transform: scale(0.85);
    }

    .info-wrapper {
      width: 100%;
      display: flex;
      align-items: center;
      .info {
        flex: 1;
        display: flex;
        flex-direction: column;
        .method-name {
          font-weight: $--font-bold;
          color: $--primary-color;
        }
        .method-estimated-date {
          font-size: $--font-2xs;
        }
        .method-description {
          max-width: 45rem;
          font-size: $--font-xs;
        }
      }
      .shipment-fee {
        color: $--primary-color;
        font-weight: $--font-bold;
        font-size: $--font-md;
      }
    }
  }
}
</style>
