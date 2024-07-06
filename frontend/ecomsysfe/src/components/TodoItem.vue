<template>
  <li>{{ itemName }}</li>
  <p>TodoItem</p>
</template>

<script lang="ts">
export default {
  //   name: 'TodoItem',
  props: ['itemName'],
};
</script>
