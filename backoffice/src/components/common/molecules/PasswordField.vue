<template>
  <div class="input-wp" :class="{ 'has-input': value && value !== '' }">
    <custom-label v-if="label" :label="label" />
    <custom-input
      class="input-password"
      :type="type"
      :value="value"
      @input="handleInput"
    />
    <span
      v-if="!visiable"
      class="icon material-symbols-outlined"
      @click="toogleVisibility"
      v-text="'visibility'"
    />
    <span
      v-else
      class="icon material-symbols-outlined"
      @click="toogleVisibility"
      v-text="'visibility_off'"
    />
  </div>
</template>

<script lang="ts">
import CustomInput from "../atomic/CustomInput.vue";
import CustomLabel from "../atomic/CustomLabel.vue";
import { defineComponent } from "vue";

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
@import "@/assets/scss/variables.scss";

:deep(.input-password) {
  padding-right: 4.5rem;
}

.icon {
  position: absolute;
  font-size: $--font-xl;
  top: 50%;
  right: 1rem;
  color: $--gray-color-300;
  transform: translateY(-50%);
  user-select: none;
  cursor: pointer;
  transition: 0.2s ease-out;
  &:hover {
    color: $--gray-color-600;
  }
}
</style>
