<template>
  <div class="input-cont">
    <label v-if="label" :class="{ required: required }">{{ label }}</label>
    <input
      ref="inputRef"
      :class="{
        validated: validated,
      }"
      :type="inputType"
      :placeholder="placeholder"
      :disabled="disabled"
      :maxlength="maxLength"
      @blur="handleValidation"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'TextField',
  props: {
    inputType: {
      type: String,
      required: false,
    },
    placeholder: {
      type: String,
      required: false,
    },
    disabled: {
      type: Boolean,
      required: false,
    },
    required: {
      type: Boolean,
      required: false,
    },
    maxLength: {
      type: Number,
      required: false,
    },
    label: {
      type: String,
      required: false,
    },
  },
  data() {
    return {
      validated: false,
    };
  },
  methods: {
    getInputRef() {
      return this.$refs.inputRef;
    },
    handleValidation(event: any) {
      this.validated = event.target.value.trim() ? true : false;
      console.log(this.validated);
    },
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.input-cont {
  width: 100%;
  label {
    display: block;
    color: $--primary-color-text;
    font-size: 1.3rem;
    font-weight: $--font-bold;
    margin-bottom: 0.5rem;
  }
  .required {
    &::after {
      content: '*';
      margin-left: 0.3rem;
      color: $--color-red;
    }
  }
  input {
    font-size: $--font-base;
    width: 100%;
    padding: 1.2rem;
    outline: none;
    color: $--primary-color-text;
    border: 1px solid $--color-border;
    transition: all 0.2s linear;
    line-height: 1;
    &:focus {
      border: 1px dotted $--black-color-900;
    }
  }
  input::-webkit-input-placeholder {
    color: $--gray-color-700;
  }

  input:-moz-placeholder {
    color: $--gray-color-700;
  }

  input::-moz-placeholder {
    color: $--gray-color-700;
  }

  input:-ms-input-placeholder {
    color: $--gray-color-700;
  }
  .validated {
    border: 1px solid $--color-valid;
  }
  .invalidated {
    border: 1px solid $--color-invalid;
  }
}
</style>
