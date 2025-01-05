<template>
  <div class="wrapper">
    <div class="color-list-wp">
      <span class="title" v-t="'productDetailPage.color'" />
      <div class="color-wp">
        <div
          v-for="color in listColorDisplay"
          class="sku"
          :class="{
            active: color.totalQuantity > 0 && color.color === currentColor,
            'out-of-stock': color.totalQuantity <= 0,
          }"
          @click="changeColor(color)"
        >
          <img :src="color.image" />
        </div>
      </div>
    </div>
    <div class="size-list-wp">
      <span class="title" v-t="'productDetailPage.size'" />
      <div class="size-wp w-full h-full flex gap-[1rem]">
        <div
          v-for="size in listSizeDisplay"
          class="sku size-item flex items-center justify-center"
          :class="{
            active: !size.disabled && size.size === currentSize,
            'out-of-stock': size.disabled,
          }"
          @click="changeSize(size)"
        >
          <span v-text="size.size" />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { ColorDisplay, ProductSkuDetail, SizeDisplay } from "@/types/worker";
import _ from "lodash";
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "ProductSkuPicker",
  emits: ["update:sku"],
  props: {
    skus: {
      type: Array as PropType<ProductSkuDetail[]>,
      default: [],
    },
    currentSku: {
      type: {} as PropType<ProductSkuDetail>,
      default: "",
    },
  },
  data() {
    return {
      currentSize: "",
      currentColor: "",
      listColorDisplay: [] as ColorDisplay[],
      listSizeDisplay: [] as SizeDisplay[],
    };
  },
  methods: {
    changeColor(color: ColorDisplay) {
      if (color.totalQuantity > 0) {
        const index = this.skus?.findIndex(
          (sku) =>
            sku.color === color.color &&
            sku.size === this.currentSize &&
            sku.quantity > 0
        );
        if (index !== undefined && index !== -1) {
          this.$emit("update:sku", this.skus?.[index]);
        } else {
          const anotherSku = this.skus?.find(
            (sku) => sku.color === color.color && sku.quantity > 0
          );
          this.$emit("update:sku", anotherSku);
        }
      }
    },
    changeSize(size: SizeDisplay) {
      if (!size.disabled) {
        const index = this.skus?.findIndex(
          (sku) =>
            sku.color === this.currentColor &&
            sku.size === size.size &&
            sku.quantity > 0
        );
        if (index !== undefined && index !== -1) {
          this.$emit("update:sku", this.skus?.[index]);
        } else {
          const anotherSku = this.skus?.find(
            (sku) => sku.size === size.size && sku.quantity > 0
          );
          this.$emit("update:sku", anotherSku);
        }
      }
    },
  },
  watch: {
    currentSku: {
      handler(sku: ProductSkuDetail) {
        this.currentColor = this.currentSku.color;
        this.currentSize = this.currentSku.size;
        this.listColorDisplay = _.reduce(
          this.skus,
          (acc: ColorDisplay[], sku) => {
            if (!acc.some((item) => item.color === sku.color)) {
              acc.push({
                color: sku.color,
                image: sku.images[0],
                totalQuantity: sku.quantity,
              });
            } else {
              const index = acc.findIndex((item) => item.color === sku.color);
              if (index !== -1) {
                const accQuantity = acc[index].totalQuantity;
                acc[index] = {
                  ...acc[index],
                  totalQuantity: accQuantity + sku.quantity,
                };
              }
            }
            return acc;
          },
          [] as ColorDisplay[]
        );
        this.listSizeDisplay = _.reduce(
          this.skus,
          (acc: SizeDisplay[], sku) => {
            if (!acc.some((item) => item.size === sku.size)) {
              acc.push({ size: sku.size, disabled: false });
            }
            return acc;
          },
          [] as SizeDisplay[]
        );
        this.listSizeDisplay = _.map(this.listSizeDisplay, (item) => {
          if (
            !this.skus?.some(
              (sku) => sku.color === this.currentColor && sku.size === item.size
            )
          ) {
            item.disabled = true;
          } else {
            const index = _.findIndex(
              this.skus,
              (sku) => sku.color === this.currentColor && sku.size === item.size
            );
            if (index !== -1 && this.skus[index].quantity <= 0) {
              item.disabled = true;
            }
          }
          return item;
        });
      },
      immediate: true,
    },
  },
  mounted() {
    console.log(this.currentSku);
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";
.wrapper {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  .title {
    font-weight: bold;
  }
  .sku {
    border: 1px solid transparent;
    cursor: pointer;
  }
  .size-item {
    width: 5rem;
    height: 5rem;
  }
  .active {
    position: relative;
    border: 1px solid $--primary-color;
    &::before {
      content: "";
      position: absolute;
      bottom: 0;
      right: 0;
      border-left: 13px solid transparent;
      border-bottom: 13px solid $--primary-color;
    }
    &::after {
      content: "\2714";
      position: absolute;
      bottom: -0.2rem;
      right: 0.1rem;
      font-size: 0.75rem;
      color: white;
    }
  }
  .out-of-stock {
    position: relative;
    opacity: 50%;
    &::before,
    &::after {
      position: absolute;
      content: "";
      top: 0;
      left: 50%;
      width: 0.1rem;
      height: 100%;
      background-color: $--primary-color;
      transform: rotate(45deg);
    }
    &::after {
      transform: rotate(-45deg);
    }
  }
  .color-list-wp {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    .color-wp {
      display: flex;
      gap: 1.5rem;

      img {
        padding: 0.2rem;
        width: 8rem;
        height: 10rem;
        object-fit: cover;
      }
    }
  }
  .size-list-wp {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
}
</style>
