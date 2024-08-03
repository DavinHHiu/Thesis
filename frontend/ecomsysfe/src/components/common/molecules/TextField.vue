<template>
  <div class="input-cont">
    <custom-input
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
import CustomInput from '../atomic/CustomInput.vue';

export default defineComponent({
  name: 'TextField',
  components: {
    CustomInput,
  },
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
}
</style>
