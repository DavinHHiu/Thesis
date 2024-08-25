<template>
  <div class="select-wp">
    <label v-if="label">{{ label }}</label>
    <select
      ref="select"
      @mousedown="handleDropdown"
      class="w-full h-[5rem]"
      :value="selectedValue"
    >
      <option>Select {{ label?.toLowerCase() }}</option>
      <option
        class="item"
        :class="{ selected: index.toString() === selectedValue }"
        @click="handleSelect"
        v-for="(item, index) in 4"
        :key="index"
        :value="index"
      >
        {{ index }}
      </option>
    </select>
    <div class="items-wp" :class="{ open: open }">
      <div
        class="item"
        :class="{ selected: index.toString() === selectedValue }"
        @click="handleSelect"
        v-for="(item, index) in 4"
        :key="index"
      >
        {{ index }}
      </div>
    </div>
    <span class="material-symbols-outlined dropdown-icon">arrow_drop_down</span>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "SelectField",
  props: {
    label: {
      type: String,
      required: false,
    },
  },
  data() {
    return {
      open: false,
      selectedValue: this.label ? "Select " + this.label?.toLowerCase() : "",
    };
  },
  methods: {
    handleDropdown(event: any) {
      event.preventDefault();
      this.open = !this.open;
      const selectField = this.$refs.select as HTMLSelectElement;
      if (selectField) {
        if (this.open) {
          selectField.focus();
        } else {
          selectField.blur();
        }
      }
    },
    handleSelect(event: any) {
      this.selectedValue = event.target.innerHTML;
      const selectField = this.$refs.select as HTMLSelectElement;
      if (selectField) {
        selectField.style.color = "#000";
      }
      this.open = false;
    },
  },
  mounted() {
    const selectField = this.$refs.select as HTMLSelectElement;
    if (selectField) {
      selectField.style.color = "#929292";
    }
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.select-wp {
  position: relative;
  label {
    position: absolute;
    top: -2rem;
    left: 1rem;
    color: $--text-color;
    font-size: $--font-xs;
  }
  select {
    border: 1px solid $--dark-alt;
    padding: 0 1.5rem;
    -webkit-appearance: none;
    -moz-appearance: none;
    -ms-appearance: none;
    appearance: none;
    outline: none;
    transition: all 0.2s linear;
    &:focus {
      border: 1px dotted $--black-color-900;
    }
    &::-ms-backdrop {
      display: none;
    }
  }
  .items-wp {
    display: none;
    height: 0;
    top: 6rem;
    width: 100%;
    position: absolute;
    background-color: $--white;
    transition: 0.5s all ease-out;
    border: 1px solid $--dark-gray;
    border-top: none;
    .item {
      display: flex;
      align-items: center;
      height: 5rem;
      padding: 0 1.5rem;
      border-top: 1px solid $--dark-gray;
      z-index: 50;
    }

    .selected,
    .item:hover {
      background-color: $--dark-gray;
      color: $--white;
    }
    .placeholder {
      color: $--gray-color-700;
    }
  }
  .open {
    display: block;
    height: auto;
  }

  .dropdown-icon {
    position: absolute;
    top: 50%;
    right: 1rem;
    font-size: $--font-4xl;
    transform: translateY(-50%);
    cursor: pointer;
  }
}
</style>
