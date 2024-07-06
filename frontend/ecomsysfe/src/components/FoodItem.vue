<template>
  <div v-on:click="countClicks">
    <h2>{{ foodName }}</h2>
    <p>{{ foodDesc }}</p>
    <p id="red">You have clicked me {{ clicks }} times.</p>
    <button @click="toogleFavourite">Toogle</button>
  </div>
</template>
<script>
export default {
  name: 'FoodItem',
  props: {
    foodName: String,
    foodDesc: String,
    isFavorite: Boolean,
  },
  data() {
    return {
      clicks: 0,
    };
  },
  methods: {
    countClicks() {
      this.clicks++;
    },
    toogleFavourite() {
      this.$emit('toogle-favourite', this.foodName);
    },
  },
};
</script>

<style>
#red {
  font-weight: bold;
  color: rgb(144, 12, 12);
}
</style>
