<template>
  <div
    ref="avatarUpload"
    @click="handleUpload"
    @drop.prevent="handleDropImage"
    @dragover.prevent
    class="upload-preview flex items-center justify-center"
  >
    <div class="upload-inner flex items-center justify-center w-full h-full">
      <img
        v-if="imagePath !== ''"
        ref="imagePreview"
        class="image-preview"
        :src="imagePath"
        alt=""
      />
      <div v-else class="flex flex-col items-center mt-[3rem] gap-[1.5rem]">
        <span @click.prevent="handleUpload" class="fa fa-images upload-icon" />
        <div class="flex flex-col items-center">
          <span class="guide" v-text="'Drag and drop image'" />
          <span class="guide link" v-text="'Or upload here'" />
        </div>
      </div>
      <input
        ref="input"
        @change="handlePreview"
        type="file"
        accept="image/*"
        class="input-file"
        @click.stop
      />
    </div>
  </div>
</template>

<script lang="ts">
import { readFileAsDataURL } from "@/utils/files";
import _ from "lodash";
import { defineComponent } from "vue";

export default defineComponent({
  name: "AvatarPreview",
  emits: ["update:modelValue"],
  props: {
    modelValue: {
      type: [String, File],
    },
  },
  data() {
    return {
      imagePath: "",
      zoomIn: {},
    };
  },
  methods: {
    handleDropImage(event: DragEvent) {
      const file = event?.dataTransfer?.files[0];
      this.$emit("update:modelValue", file);
    },
    handleUpload(event: any) {
      const input = this.$refs.input as HTMLInputElement;
      if (input) {
        input.click();
      }
    },
    handlePreview(event: any) {
      const file = event.target.files[0];
      this.$emit("update:modelValue", file);
    },
    async getDataURL(file: File) {
      this.imagePath = await readFileAsDataURL(file);
    },
  },
  computed: {
    uploadWrapper() {
      return this.$refs.uploadWrapper as HTMLDivElement;
    },
  },
  watch: {
    modelValue(newValue) {
      if (newValue) {
        if (newValue instanceof File) {
          this.getDataURL(newValue);
        } else if (typeof newValue === "string") {
          this.imagePath = newValue;
        }
      }
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.upload-preview {
  width: 100%;
  height: 35rem;
  border-radius: 0.8rem;
  border: 1px solid $--gray-color-200;
  padding: 0.7rem;
  box-shadow: $--shadow;
  overflow: hidden;
  .upload-inner {
    position: relative;
    background-color: $--gray-color-150;
    border: 1px solid $--gray-color-200;
    border-radius: 0.4rem;
    overflow: hidden;
  }
  .image-preview {
    object-fit: cover;
    object-position: center;
  }
  .link {
    color: $--color-blue;
    cursor: pointer;
  }
  .upload-icon {
    color: $--color-blue;
    font-size: $--font-7xl;
  }
  .input-file {
    display: none;
  }
}
</style>
