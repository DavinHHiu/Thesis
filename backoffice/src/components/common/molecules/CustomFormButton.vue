<template>
  <div class="flex gap-[2rem]">
    <custom-button
      class="w-[15rem]"
      @click="$emit('update')"
      v-text="textButton"
    />
    <custom-button
      class="w-[15rem]"
      intent="second"
      @click="$emit('back')"
      v-text="$t('buttonLabel.back')"
    />
  </div>
</template>

<script lang="ts">
import CustomButton from "../atomic/CustomButton.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "CustomFormButton",
  emits: ["update", "back"],
  components: {
    CustomButton,
  },
  props: {
    textButton: {
      type: String,
      required: true,
    },
  },
});
</script>
