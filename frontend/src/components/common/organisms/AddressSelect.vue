<template>
  <div>
    <div ref="wrapper" class="wrapper" @click="toggleDropdown">
      <div class="select-display">
        <span class="material-symbols-outlined" v-text="'pin_drop'" />
        <div class="info">
          <span>
            <span
              class="representative"
              v-text="addresses[curIdx].representative"
            />
            <span v-text="` | ${addresses[curIdx].tel}`" />
            <span
              class="icon-edit material-symbols-outlined"
              v-text="'border_color'"
              @click.stop="handleEdit(addresses[curIdx].id as number)"
            />
          </span>
          <span class="address" v-text="addresses[curIdx].address_1" />
          <span
            class="address"
            v-text="
              `${addresses[curIdx].ward}, ${addresses[curIdx].district}, ${addresses[curIdx].city} `
            "
          />
        </div>
        <span
          v-if="addresses.length > 1"
          class="material-symbols-outlined icon-dropdown"
          :class="{ rotate: open }"
          v-text="'keyboard_arrow_up'"
        />
      </div>
      <div class="select-dropdown" :class="{ open }">
        <div
          class="dropdown-item"
          v-for="address in dropdownItems"
          :key="address.id"
          @click.stop.prevent="chooseAddress(address.id as number)"
        >
          <span
            class="material-symbols-outlined icon-location"
            v-text="'pin_drop'"
          />
          <div class="info">
            <span>
              <span class="representative" v-text="address.representative" />
              <span v-text="` | ${address.tel}`" />
              <span
                class="icon-edit material-symbols-outlined"
                v-text="'border_color'"
                @click.stop="handleEdit(address.id as number)"
              />
            </span>
            <span class="address" v-text="address.address_1" />
            <span
              class="address"
              v-text="`${address.ward}, ${address.district}, ${address.city} `"
            />
          </div>
        </div>
      </div>
    </div>
    <div
      class="action-wp flex items-center justify-center gap-[0.5rem] mt-[1rem]"
    >
      <span
        v-if="addresses.length < 5 && openAddBtn"
        class="add-icon material-symbols-outlined"
        v-text="'add_circle'"
      />
      <span
        v-if="addresses.length < 5 && openAddBtn"
        class="add-label"
        v-text="'Add new address'"
        @click="addNewAddress"
      />
      <span
        class="add-note mt-[1rem]"
        v-text="`Maximum ${addresses.length}/5`"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { useAddressStore } from "@/stores/address";
import { Address } from "@/types/worker";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "AddressSelect",
  emits: ["add:address", "edit:address"],
  props: {
    openAddBtn: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      open: false,
      curIdx: 0,
    };
  },
  computed: {
    ...mapState(useAddressStore, ["address", "addresses"]),
    dropdownItems() {
      return this.addresses.filter((_, index) => index !== this.curIdx);
    },
  },
  methods: {
    ...mapActions(useAddressStore, ["setAddress"]),
    toggleDropdown() {
      if (this.addresses.length > 0) {
        this.open = !this.open;
      }
    },
    chooseAddress(id: number) {
      this.curIdx = this.addresses.findIndex((address) => address.id === id);
      this.setAddress(this.addresses[this.curIdx]);
      this.toggleDropdown();
    },
    addNewAddress() {
      this.open = false;
      this.$emit("add:address");
    },
    handleEdit(id: number) {
      this.open = false;
      this.curIdx = this.addresses.findIndex((address) => address.id === id);
      this.$emit("edit:address", id);
    },
  },
  mounted() {
    console.log(this.curIdx);
    this.setAddress(this.addresses[this.curIdx]);
  },
  watch: {
    addresses: {
      immediate: true,
      handler(newVal) {
        if (newVal.length > 0) {
          this.curIdx = 0;
          this.setAddress(newVal[this.curIdx]);
        }
      },
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.wrapper {
  width: 100%;
  background-color: $--gray-color-150;
  overflow: hidden;

  .select-display {
    display: flex;
    align-items: center;
    gap: 1rem;
    width: 100%;
    height: 9rem;
    padding: 1rem 2rem;
    color: $--gray-color-900;
    border: 1px solid $--primary-color;
    cursor: pointer;

    &:hover {
      .icon-edit {
        opacity: 1;
        visibility: visible;
      }
    }

    .icon-dropdown {
      transition: 0.35s ease-in-out;
      &.rotate {
        transform: rotate(180deg);
      }
    }
  }
  .info {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    .representative {
      font-weight: $--font-bold;
      color: $--primary-color;
    }
    .address {
      font-size: $--font-2xs;
    }
  }
  .select-dropdown {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    max-height: 0;
    opacity: 0;
    overflow: hidden;
    transition: all 0.35s linear;
    cursor: pointer;
    color: $--gray-color-900;

    &.open {
      max-height: 45rem;
      opacity: 1;
    }

    .dropdown-item {
      height: 9rem;
      display: flex;
      padding: 1rem 2rem;
      align-items: center;
      gap: 1rem;
      border-top: 1px solid $--color-border;
      user-select: none;
      cursor: pointer;
      &:hover {
        .icon-edit {
          opacity: 1;
          visibility: visible;
        }
      }
    }

    .icon-location {
      visibility: hidden;
    }
  }
  .icon-edit {
    opacity: 0;
    visibility: hidden;
    margin-left: 1rem;
    font-size: $--font-xs;
    color: $--gray-color-600;
    transition: all 0.25s ease-in-out;
    &:hover {
      color: $--primary-color;
      transform: scale(1.5);
    }
  }
}
.action-wp {
  position: relative;
  span {
    display: block;
    font-size: $--font-2xs;
    cursor: pointer;
    &:hover {
      text-decoration: underline;
    }
  }
  .add-icon {
    font-size: $--font-xs;
  }
  .add-note {
    position: absolute;
    right: 0;
    color: $--gray-color-400;
  }
}
</style>
