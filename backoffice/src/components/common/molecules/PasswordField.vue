<template>
  <div class="input-wp" :class="{ 'has-input': value != '' }">
    <custom-label v-if="label" v-text="label" />
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
    >
      visibility
    </span>
    <span
      v-else
      class="icon material-symbols-outlined"
      @click="toogleVisibility"
    >
      visibility_off
    </span>
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
  top: 50%;
  right: 1rem;
  color: $--gray-color-700;
  transform: translateY(-50%);
  user-select: none;
  cursor: pointer;
}
</style>
