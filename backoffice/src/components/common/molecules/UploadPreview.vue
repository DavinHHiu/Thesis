<template>
  <div>
    <div
      ref="uploadWrapper"
      @click="handleUpload"
      @drop.prevent="handleDropImage"
      @dragover.prevent
      class="upload-preview flex items-center justify-center"
      :class="intent"
    >
      <div
        class="upload-inner flex items-center justify-center w-full h-full"
        @mousemove="handleZoom"
        @mouseout="handleNotZoom"
      >
        <img
          v-if="imagePath !== ''"
          ref="imagePreview"
          class="image-preview"
          :src="imagePath"
          alt=""
        />
        <img
          v-if="imagePath !== ''"
          ref="imageZoom"
          class="image-zoom"
          :src="imagePath"
          alt=""
          :style="zoomIn"
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
        />
      </div>
    </div>
    <div v-if="images" class="image-thumb-wp">
      <div
        v-for="(image, index) in images"
        :key="index"
        class="image-thumb"
        @click="changeImage(index)"
      >
        <img
          :src="image"
          alt=""
          :class="{ 'cur-image': index === curImgIdx }"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { readFileAsDataURL } from "@/utils/files";
import _ from "lodash";
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "UploadPreview",
  emits: ["update:modelValue"],
  props: {
    modelValue: {
      type: Array as PropType<File[] | String[]>,
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
      images: [] as string[],
      curImgIdx: 0,
      zoomIn: {},
    };
  },
  methods: {
    handleDropImage(event: DragEvent) {
      const files = event?.dataTransfer?.files;
      this.images = [];
      if (files) {
        _.forEach(files, (file) => {
          readFileAsDataURL(file).then((result) => {
            if (this.images.length < 10) {
              this.images.push(result);
            }
          });
        });
        this.$emit("update:modelValue", files);
      }
    },
    handleUpload(event: any) {
      const input = this.$refs.input as HTMLInputElement;
      if (input) {
        input.click();
      }
    },
    handlePreview(event: any) {
      const files = event.target.files;
      this.images = [];
      if (files) {
        _.forEach(files, (file) => {
          readFileAsDataURL(file).then((result) => {
            if (this.images.length < 10) {
              this.images.push(result);
            }
          });
        });

        this.$emit("update:modelValue", files);
      }
    },
    changeImage(index: number) {
      this.curImgIdx = index;
      this.imagePath = this.images[this.curImgIdx];
    },
    handleZoom(event: MouseEvent) {
      let pointer = {
        x:
          (event.offsetX * 100) /
          (this.$refs.imageZoom as HTMLImageElement).offsetWidth,
        y:
          (event.offsetY * 100) /
          (this.$refs.imageZoom as HTMLImageElement).offsetHeight,
        w: (this.$refs.imageZoom as HTMLImageElement).offsetWidth,
        h: (this.$refs.imageZoom as HTMLImageElement).offsetHeight,
      };
      this.zoomIn = {
        display: "block",
        "object-position": `${pointer.x}% ${pointer.y}%`,
      };
      console.log(pointer);
      console.log(event);
      console.log(`${pointer.x}% ${pointer.y}%`);
    },
    handleNotZoom(event: MouseEvent) {
      this.zoomIn = {
        display: "none",
      };
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
        if (newValue instanceof FileList) {
          this.getUserAvatarDataURL(newValue[0]);
        } else if (newValue instanceof Array) {
          this.imagePath = newValue[0];
          this.images = newValue;
        }
      }
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.upload-preview {
  background-color: #fff;
  border: 1px solid $--gray-color-200;
  border-radius: 0.8rem;
  padding: 0.7rem;
  box-shadow: $--shadow;
  .upload-inner {
    position: relative;
    background-color: #eee;
    border: 1px solid $--gray-color-200;
    border-radius: 0.4rem;
    overflow: hidden;
  }
  .image-preview {
    height: 100%;
    width: 100%;
    object-fit: cover;
    object-position: center;
  }
  .image-zoom {
    position: absolute;
    width: 200%;
    height: 200%;
    object-fit: cover;
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

.poster {
  width: 40rem;
  height: 50rem;
}

.avatar {
  width: 30rem;
  height: 30rem;
  border-radius: 50%;
  overflow: hidden;
}

.image-thumb-wp {
  margin-top: 1rem;
  display: flex;
  width: 40rem;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 1rem;
  img {
    width: 7rem;
    height: 7rem;
    object-fit: cover;
    object-position: center;
    border-radius: 1rem;
    transition: 0.2s all ease-out;
    border: 2px solid transparent;
    cursor: pointer;
    &:active {
      transform: scale(0.8);
    }
  }
  .cur-image {
    border: 2px solid $--color-danger;
  }
}
</style>
