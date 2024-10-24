<template>
  <div class="flex gap-[3rem]">
    <div class="list-thumb-images flex flex-col gap-[2rem]">
      <div
        v-for="(image, index) in images"
        :key="index"
        class="image-thumb"
        :class="{
          active: index === currentIndex,
        }"
        @click="changeImage(index)"
      >
        <img :src="String(image)" class="w-full h-full" />
      </div>
    </div>
    <div
      ref="imagePreviewWp"
      class="image-preview"
      @mousemove="previewImage"
      @mouseleave="offZoom"
    >
      <img :src="String(images?.[currentIndex])" />
      <div ref="imageZoom" class="zoom-img" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "ImagePreview",
  props: {
    images: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      currentIndex: 0,
    };
  },
  methods: {
    changeImage(index: number) {
      this.currentIndex = index;
      this.updateBackgroundImage();
    },
    previewImage(e: MouseEvent) {
      const imagePreviewWp = this.$refs.imagePreviewWp as HTMLDivElement;
      const imageZoom = this.$refs.imageZoom as HTMLImageElement;

      const x = e.offsetX;
      const y = e.offsetY;
      const width = imagePreviewWp.getBoundingClientRect().width;
      const height = imagePreviewWp.getBoundingClientRect().height;

      imageZoom.style.display = "block";
      imageZoom.style.backgroundPosition = `${(x / width) * 100}% ${(y / height) * 100}%`;
    },
    offZoom() {
      console.log("out");
      const imageZoom = this.$refs.imageZoom as HTMLImageElement;
      imageZoom.style.display = "none";
    },
    updateBackgroundImage() {
      const imageZoom = this.$refs.imageZoom as HTMLImageElement;
      imageZoom.style.backgroundImage = `url("${String(this.images?.[this.currentIndex])}")`;
    },
  },
  watch: {
    images() {
      this.updateBackgroundImage();
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.list-thumb-images {
  .image-thumb {
    width: 9rem;
    height: 11rem;
    border: 1px transparent;
    cursor: pointer;
    &.active {
      border: 1px solid $--color-danger;
    }
  }
}
.image-preview {
  position: relative;
  overflow: hidden;
  cursor: zoom-in;
  .zoom-img {
    display: none;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: 200%;
    object-fit: cover;
  }
}
</style>
