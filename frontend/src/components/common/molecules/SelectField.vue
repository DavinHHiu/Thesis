<template>
  <div class="select-wp">
    <label v-if="label" v-text="label" />
    <select
      ref="select"
      @mousedown="openDropdown"
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
        class="item flex items-center gap-[1rem]"
        :class="{ selected: option.value === value }"
        v-for="(option, index) in options"
        :key="index"
        @click="selectOption(option.value)"
      >
        <img v-if="option.image" :src="option.image" />
        <span v-text="option.displayValue" />
      </div>
    </div>
    <span class="material-symbols-outlined dropdown-icon" @click="openDropdown"
      >arrow_drop_down</span
    >
  </div>
</template>

<script lang="ts">
import { OptionItem } from "@/types/frontend";
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
@import "@/assets/variables";

.select-wp {
  position: relative;
  label {
    position: absolute;
    top: -2.5rem;
    left: 1rem;
    color: $--primary-color-text;
    font-size: $--font-sm;
    font-weight: $--font-semibold;
  }
  select {
    border: 1px solid $--title-color-text;
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
    background-color: $--white-color-900;
    transition: 0.5s all ease-out;
    border: 1px solid $--dark-gray;
    border-top: none;
    z-index: 50;
    .item {
      height: 5rem;
      padding: 0 1.5rem;
      border-top: 1px solid $--dark-gray;
      cursor: pointer;
      img {
        height: 90%;
      }
    }

    .selected,
    .item:hover {
      background-color: $--dark-gray;
      color: $--white-color-900;
    }
    .placeholder {
      color: $--gray-color-700;
    }
  }

  .dropdown-icon {
    position: absolute;
    display: inline-block;
    top: 50%;
    right: 0.5rem;
    font-size: $--font-2xl;
    transform: translateY(-50%);
    user-select: none;
    cursor: pointer;
  }
}
</style>
