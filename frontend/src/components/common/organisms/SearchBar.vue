<template>
  <div class="wrapper flex flex-col items-end gap-[1rem]">
    <select-field
      class="search-engine-select w-full"
      :options="options"
      :value="curOption"
      @update:model-value="(option) => (curOption = option)"
    />
    <upload-preview
      :class="{ 'upload-open': curOption === 'image' }"
      class="upload-preview"
      v-model="imageSearch"
      @update:model-value="uploadImageSearch"
    />
    <text-field
      v-if="curOption === 'text'"
      class="w-full"
      :label="'searchPage.placeholder'"
    />
    <custom-button
      class="w-full h-[5rem]"
      intent="primary"
      v-text="'Search'"
      @click="handleSearch"
    />
  </div>
</template>
<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import SelectField from "@/components/common/molecules/SelectField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import UploadPreview from "@/components/common/molecules/UploadPreview.vue";
import IconRightArrow from "@/components/icons/IconRightArrow.vue";
import { OptionItem } from "@/types/frontend";
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "SearchBar",
  emits: ["update:modelValue", "submit"],
  props: {
    modelValue: {
      type: Object as PropType<String | File>,
      required: true,
    },
  },
  components: {
    CustomButton,
    TextField,
    IconRightArrow,
    SelectField,
    UploadPreview,
  },
  data() {
    return {
      options: [
        { displayValue: "By text", value: "text" },
        { displayValue: "By image", value: "image" },
      ] as OptionItem[],
      curOption: "text" as string,
      imageSearch: File,
    };
  },
  methods: {
    uploadImageSearch(newValue: File) {
      this.$emit("update:modelValue", newValue);
    },
    handleSearch() {
      this.$emit("submit");
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.wrapper {
  .upload-preview {
    margin-top: -1rem;
    height: 0rem;
    border: none;
    padding: 0;
    opacity: 0;
    visibility: hidden;
    transition: 0.2s all ease-out;
  }
  .upload-open {
    margin-top: 0;
    height: 35rem;
    opacity: 100;
    visibility: visible;
    border: 1px solid $--gray-color-200;
    padding: 0.7rem;
  }
}
</style>
