<template>
  <card-view class="h-[280px] w-full mt-[20px] container" padding="10px">
    <div class="title" v-if="title">{{ title }}</div>
    <image-slider
      class="h-[200px] w-full"
      :slides="[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7]"
      :items-per-slide="4"
    >
      <img
        src="https://m.media-amazon.com/images/I/61oSwPvRWLL._AC_SY200_.jpg"
        class="w-[270px]"
      />
      <img
        src="https://m.media-amazon.com/images/I/61oSwPvRWLL._AC_SY200_.jpg"
        class="w-[270px]"
      />
      <img
        src="https://m.media-amazon.com/images/I/61oSwPvRWLL._AC_SY200_.jpg"
        class="w-[270px]"
      />
      <img
        src="https://m.media-amazon.com/images/I/61oSwPvRWLL._AC_SY200_.jpg"
        class="w-[270px]"
      />
      <img
        src="https://m.media-amazon.com/images/I/61oSwPvRWLL._AC_SY200_.jpg"
        class="w-[270px]"
      />
      <img
        src="https://m.media-amazon.com/images/I/61oSwPvRWLL._AC_SY200_.jpg"
        class="w-[270px]"
      />
      <img
        src="https://m.media-amazon.com/images/I/61oSwPvRWLL._AC_SY200_.jpg"
        class="w-[270px]"
      />
      <img
        src="https://m.media-amazon.com/images/I/61oSwPvRWLL._AC_SY200_.jpg"
        class="w-[270px]"
      />
      <img
        src="https://m.media-amazon.com/images/I/61oSwPvRWLL._AC_SY200_.jpg"
        class="w-[270px]"
      />
      <img
        src="https://m.media-amazon.com/images/I/61oSwPvRWLL._AC_SY200_.jpg"
        class="w-[270px]"
      />
      <img
        src="https://m.media-amazon.com/images/I/61oSwPvRWLL._AC_SY200_.jpg"
        class="w-[270px]"
      />
      <img
        src="https://m.media-amazon.com/images/I/61oSwPvRWLL._AC_SY200_.jpg"
        class="w-[270px]"
      />
      <img
        src="https://m.media-amazon.com/images/I/61oSwPvRWLL._AC_SY200_.jpg"
        class="w-[270px]"
      />
      <img
        src="https://m.media-amazon.com/images/I/61oSwPvRWLL._AC_SY200_.jpg"
        class="w-[270px]"
      />
      <img
        src="https://m.media-amazon.com/images/I/61oSwPvRWLL._AC_SY200_.jpg"
        class="w-[270px]"
      />
      <img
        src="https://m.media-amazon.com/images/I/61oSwPvRWLL._AC_SY200_.jpg"
        class="w-[270px]"
      />
    </image-slider>
  </card-view>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import CardView from './CardView.vue';
import ImageSlider from './ImageSlider.vue';

export default defineComponent({
  name: 'ItemSlider',
  components: {
    CardView,
    ImageSlider,
  },
  data() {
    return {};
  },
  props: {
    title: {
      type: String,
      required: true,
    },
  },
  methods: {},
  computed: {},
  mounted() {},
});
</script>

<style scoped>
.container {
  padding: 20px;
}

.title {
  font-size: 21px;
  padding-left: 10px;
  font-weight: bold;
}
</style>
