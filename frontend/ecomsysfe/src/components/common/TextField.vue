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

<style scoped>
.input-cont {
  width: 100%;
  label {
    display: block;
    color: #000;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 5px;
  }
  .required {
    &::after {
      content: '*';
      margin-left: 3px;
      color: #ff0000;
    }
  }
  input {
    font-size: 15px;
    width: 100%;
    padding: 12px;
    outline: none;
    color: #000;
    border: 1px solid #e2e2e2;
    transition: all 0.2s linear;
    line-height: 1;
    &:focus {
      border: 1px dotted #000;
    }
  }
  input::-webkit-input-placeholder {
    color: #999;
  }

  input:-moz-placeholder {
    color: #999;
  }

  input::-moz-placeholder {
    color: #999;
  }

  input:-ms-input-placeholder {
    color: #999;
  }
  .validated {
    border: 1px solid #69bf29;
  }
  .invalidated {
    border: 1px solid #d65d67;
  }
}
</style>
