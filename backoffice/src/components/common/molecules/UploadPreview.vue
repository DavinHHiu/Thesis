<template>
  <div
    ref="uploadWrapper"
    @click="handleUpload"
    class="upload-preview flex items-center justify-center h-[40rem]"
    :class="intent"
  >
    <img
      v-if="imagePath !== ''"
      ref="imagePreview"
      class="image-preview"
      :src="imagePath"
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
import { readFileAsDataURL } from "@/utils/files";
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "UploadPreview",
  emits: ["update:modelValue"],
  props: {
    modelValue: {
      type: [File, String] as PropType<File | String>,
    },
    intent: {
      type: String,
      default: "poster",
      validator: (value: string) => {
        return ["poster", "avatar"].includes(value);
      },
    },
  },
  data() {
    return {
      imagePath: "",
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
        this.$emit("update:modelValue", file);
      }
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
        this.uploadWrapper.style.border = "none";
        if (typeof newValue === "string") {
          this.imagePath = newValue;
        } else if (newValue instanceof File) {
          this.getUserAvatarDataURL(newValue);
        }
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
    height: 100%;
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

.poster {
  width: 30rem;
  height: 40rem;
}

.avatar {
  width: 30rem;
  height: 30rem;
  border-radius: 50%;
  overflow: hidden;
}
</style>
