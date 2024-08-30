<template>
  <div
    ref="uploadWrapper"
    @click="handleUpload"
    class="upload-preview flex items-center justify-center h-[40rem]"
  >
    <img
      v-if="src !== ''"
      ref="imagePreview"
      class="image-preview"
      :src="src"
      alt=""
    />
    <span v-else @click="handleUpload" class="material-symbols-outlined"
      >image</span
    >
    <input
      ref="input"
      @change="handlePreview"
      type="file"
      accept="image/*"
      class="input-file"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "UploadPreview",
  data() {
    return {
      file: undefined as File | undefined,
      src: "",
    };
  },
  methods: {
    handleUpload(event: any) {
      event.stopPropagation();
      const input = this.$refs.input as HTMLInputElement;
      if (input) {
        input.click();
      }
    },
    handlePreview(event: any) {
      const file = event.target.files[0];
      if (file) {
        this.file = file;
        const reader = new FileReader();

        reader.onload = (event: any) => {
          const uploadWrapper = this.$refs.uploadWrapper as HTMLDivElement;
          if (uploadWrapper) {
            this.src = event.target.result;
            uploadWrapper.style.border = "none";
          }
        };

        reader.readAsDataURL(file);
      }
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.upload-preview {
  border: 1px dashed $--gray-color-700;
  .image-preview {
    height: 40rem;
    width: 100%;
    max-width: 30rem;
    object-fit: cover;
    object-position: center;
  }
  span {
    font-size: $--font-9xl;
    cursor: pointer;
  }
  .input-file {
    display: none;
  }
}
</style>
