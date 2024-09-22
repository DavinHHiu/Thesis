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
      <span
        v-else
        @click.prevent="handleUpload"
        class="fa fa-images upload-icon"
      />
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
    getUserAvatarDataURL(file: File) {
      readFileAsDataURL(file).then((result) => (this.imagePath = result));
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
          this.getUserAvatarDataURL(newValue);
        } else if (typeof newValue === "string") {
          this.imagePath = newValue;
        }
      }
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.upload-preview {
  width: 30rem;
  height: 30rem;
  border-radius: 50%;
  background-color: #fff;
  border: 1px solid $--gray-color-200;
  padding: 0.7rem;
  box-shadow: $--shadow;
  overflow: hidden;
  .upload-inner {
    position: relative;
    background-color: #eee;
    border: 1px solid $--gray-color-200;
    border-radius: 50%;
    overflow: hidden;
  }
  .image-preview {
    height: 100%;
    width: 100%;
    object-fit: cover;
    object-position: center;
  }
  span {
    font-size: $--font-7xl;
    color: #ccc;
    cursor: pointer;
  }
  .input-file {
    display: none;
  }
}
</style>
