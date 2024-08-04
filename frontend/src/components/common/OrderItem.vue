<template>
  <tr class="item-cont">
    <td class="item-id">OR6789</td>
    <td class="item-image">
      <img
        src="https://websitedemos.net/brandstore-02/wp-content/uploads/sites/150/2021/03/sports-shoe3-300x300.jpg"
      />
    </td>

    <td class="item-shipping-method">Express</td>
    <td class="item-delivery">Tue 01/01/2025</td>
    <td class="item-status">Shipping</td>
    <td class="item-payment-method">COD</td>
    <td class="item-total-amount">$150.00</td>
    <td class="item-list-product">Show list products</td>
  </tr>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'OrderItem',
});
</script>

<style scoped>
.item-cont {
  display: flex;
  align-items: center;
}
</style>
