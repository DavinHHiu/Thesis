<template>
  <div class="badge-wp">
    <div class="badge-bg">
      <span v-for="(_, idx) in 5" :key="idx" class="fa fa-star"></span>
    </div>
    <div class="badge-fg" :style="ratingStar">
      <div class="badge-inner">
        <span v-for="(_, idx) in 5" :key="idx" class="fa fa-star gold"></span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "BadgeStar",
  props: {
    rating: {
      type: Number,
      required: true,
      validator: (val: number) => {
        return val >= 0 && val <= 5;
      },
    },
  },
  computed: {
    ratingStar() {
      let rate = 0;
      if (this.rating) {
        rate = (this.rating / 5) * 100;
        rate = rate > 100 ? 100 : rate < 0 ? 0 : rate;
      }
      return {
        width: `${rate}%`,
      };
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.badge-wp {
  position: relative;
  display: inline-block;

  .badge-bg {
    color: $--color-disabled;
  }

  .badge-fg {
    position: absolute;
    top: 0;
    left: 0;
    white-space: nowrap;
    overflow: hidden;
    .badge-inner {
      .gold {
        color: $--color-gold;
      }
    }
  }
}
</style>
