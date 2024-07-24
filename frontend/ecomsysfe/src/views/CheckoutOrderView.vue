<template>
  <div class="wrapper">
    <section class="order-detail">
      <h2 class="section-title">Order details</h2>
      <table class="order-detail-content">
        <thead>
          <tr>
            <th>Product</th>
            <th>Total</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Basic Gray Jeans × 1</td>
            <td>$150.00</td>
          </tr>
        </tbody>
        <tfoot>
          <tr>
            <td>Subtotal:</td>
            <td>$150.00</td>
          </tr>
          <tr>
            <td>Payment method:</td>
            <td>Direct bank transfer</td>
          </tr>
          <tr>
            <td>Total:</td>
            <td>$150.00</td>
          </tr>
        </tfoot>
      </table>
    </section>
    <section class="billing-address">
      <h2 class="section-title">Billing address</h2>
      <div class="custom-info-wp">
        <p>Nguyễn Hiếu</p>
        <p>Nghĩa Dũng</p>
        <p>Hà Nội 000084</p>
        <p>Vietnam</p>
        <p>0815220802</p>
        <p>honghieu2208@gmail.com</p>
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'CheckoutOrderView',
  components: {},
});
</script>

<style scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  gap: 35px;
  .section-title {
    width: 100%;
    padding: 21px;
    font-size: 21px;
    font-weight: 600;
    border: 1px solid #e2e2e2;
  }
  .order-detail-content {
    margin-top: -1px;
    font-size: 16px;
    color: #000;
    width: 100%;
    thead tr {
      border: 1px solid #e2e2e2;
    }
    th,
    td {
      padding: 11px 16px;
    }
    td {
      border: 1px solid #e2e2e2;
    }
    th {
      text-align: left;
      font-weight: 600;
    }
  }
  .custom-info-wp {
    display: flex;
    color: #000;
    flex-direction: column;
    margin-top: -1px;
    font-size: 16px;
    padding: 16px;
    border: 1px solid #e2e2e2;
    gap: 5px;
  }
}
</style>
