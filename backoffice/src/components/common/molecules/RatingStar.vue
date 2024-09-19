<template>
  <div class="rating-wp">
    <input type="radio" name="rating" id="rating1" />
    <label for="rating1" class="fa fa-star"></label>
    <input type="radio" name="rating" id="rating2" />
    <label for="rating2" class="fa fa-star"></label>
    <input type="radio" name="rating" id="rating3" />
    <label for="rating3" class="fa fa-star"></label>
    <input type="radio" name="rating" id="rating4" />
    <label for="rating4" class="fa fa-star"></label>
    <input type="radio" name="rating" id="rating5" />
    <label for="rating5" class="fa fa-star"></label>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({});
</script>

<style lang="scss" scoped>
.rating-wp {
  input {
    display: none;
  }
  label {
    color: #ffe400;
    font-size: 2rem;
  }
  input,
  label {
    text-shadow: 1px 1px 0 #ffe400;
    cursor: pointer;
  }
  input:checked + label ~ label {
    color: #838383;
  }
}
</style>
