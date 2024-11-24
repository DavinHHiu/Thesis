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
      :model-value="imageSearch"
      @update:model-value="(file) => (imageSearch = file)"
    />
    <text-field
      v-if="curOption === 'text'"
      class="w-full"
      :label="'searchPage.placeholder'"
    />
    <custom-button class="w-full h-[5rem]" intent="primary" v-text="'Search'" />
  </div>
</template>
<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import SelectField from "@/components/common/molecules/SelectField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import UploadPreview from "@/components/common/molecules/UploadPreview.vue";
import IconRightArrow from "@/components/icons/IconRightArrow.vue";
import { OptionItem } from "@/types/frontend";
import { defineComponent } from "vue";

export default defineComponent({
  name: "SearchBar",
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
