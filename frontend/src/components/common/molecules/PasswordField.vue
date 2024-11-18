<template>
  <div class="input-wp" :class="{ 'has-input': value != '' }">
    <custom-label v-if="label" v-t="label" />
    <custom-input
      class="input-password"
      :type="type"
      :value="value"
      @input="handleInput"
    />
    <span
      v-if="!visiable"
      class="icon material-symbols-outlined"
      v-text="'visibility'"
      @click="toogleVisibility"
    />
    <span
      v-else
      class="icon material-symbols-outlined"
      v-text="'visibility_off'"
      @click="toogleVisibility"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

import CustomInput from "../atomic/CustomInput.vue";
import CustomLabel from "../atomic/CustomLabel.vue";

export default defineComponent({
  name: "PasswordField",
  emits: ["update:modelValue"],
  components: {
    CustomLabel,
    CustomInput,
  },
  props: {
    label: {
      type: String,
      required: false,
    },
    value: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      visiable: false,
      type: "password",
    };
  },
  methods: {
    handleInput(event: any) {
      const value = event.target.value;
      this.$emit("update:modelValue", value);
    },
    toogleVisibility() {
      this.visiable = !this.visiable;
      this.type = this.visiable ? "text" : "password";
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/_variables.scss";

:deep(.input-password) {
  padding-right: 4.5rem;
}

.icon {
  position: absolute;
  top: 50%;
  right: 1rem;
  color: $--gray-color-500;
  transform: translateY(-50%);
  user-select: none;
  cursor: pointer;
}
</style>
