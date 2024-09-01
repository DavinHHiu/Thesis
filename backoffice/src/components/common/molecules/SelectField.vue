<template>
  <div class="select-wp">
    <label v-if="label" v-text="label" />
    <select
      ref="select"
      @mousedown.stop="openDropdown"
      class="w-full h-[5rem]"
      :value="value"
    >
      <option value="" disabled selected>
        Select {{ label?.toLowerCase() }}
      </option>
      <option
        v-for="(option, index) in options"
        :key="index"
        :value="option.value"
        v-text="option.displayValue"
      />
    </select>
    <div ref="itemsWp" class="items-wp">
      <div
        class="item"
        :class="{ selected: option.value === value }"
        v-for="(option, index) in options"
        :key="index"
        @click="selectOption(option.value)"
        v-text="option.displayValue"
      />
    </div>
    <span class="material-symbols-outlined dropdown-icon">arrow_drop_down</span>
  </div>
</template>

<script lang="ts">
import { OptionItem } from "@/types/backoffice";
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "SelectField",
  emits: ["update:modelValue"],
  props: {
    label: {
      type: String,
      required: false,
    },
    options: {
      type: Array as PropType<OptionItem[]>,
      required: true,
    },
    value: {
      type: String,
      required: false,
    },
  },
  data() {},
  methods: {
    openDropdown(event: Event) {
      event.preventDefault();
      this.open();
    },
    selectOption(value: string) {
      this.$emit("update:modelValue", value);
      if (this.selectElement) {
        this.selectElement.style.color = "#000";
      }
      this.close();
    },
    handleFocusOut(event: Event) {
      const element = event.target as HTMLElement;
      if (
        element !== this.selectElement &&
        !this.dropdownElemnent.contains(element)
      ) {
        this.close();
      }
    },
    open() {
      this.dropdownElemnent.style.display = "block";
      this.selectElement.focus();
      document.addEventListener("mousedown", this.handleFocusOut);
    },
    close() {
      this.dropdownElemnent.style.display = "none";
      document.removeEventListener("mousedown", this.handleFocusOut);
    },
  },
  computed: {
    selectElement(): HTMLSelectElement {
      return this.$refs.select as HTMLSelectElement;
    },
    dropdownElemnent(): HTMLDivElement {
      return this.$refs.itemsWp as HTMLDivElement;
    },
  },
  watch: {
    value() {
      this.selectElement.style.color = "#000";
    },
  },
  mounted() {
    if (!this.value && this.selectElement) {
      this.selectElement.style.color = "#929292";
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
    top: -2.5rem;
    left: 1rem;
    color: $--text-color;
    font-size: $--font-sm;
    font-weight: $--font-semibold;
  }
  select {
    border: 1px solid $--dark-alt;
    padding: 0 1.5rem;
    transition: all 0.2s linear;
    &:focus {
      border: 1px dotted $--black-color-900;
    }
  }
  .items-wp {
    display: none;
    top: 6rem;
    height: auto;
    width: 100%;
    position: absolute;
    background-color: $--white;
    transition: 0.5s all ease-out;
    border: 1px solid $--dark-gray;
    border-top: none;
    z-index: 50;
    .item {
      display: flex;
      align-items: center;
      height: 5rem;
      padding: 0 1.5rem;
      border-top: 1px solid $--dark-gray;
      cursor: pointer;
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
