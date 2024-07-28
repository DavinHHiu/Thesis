<template>
  <div class="wrapper">
    <p>Thank you. Your order has been received.</p>
    <ul class="order-info">
      <li class="order-info-item">
        ORDER NUMBER:
        <strong>6261</strong>
      </li>
      <li class="order-info-item">
        DATE:
        <strong>July 28, 2024</strong>
      </li>
      <li class="order-info-item">
        TOTAL:
        <strong>$150.00</strong>
      </li>
      <li class="order-info-item">
        PAYMENT METHOD:
        <strong>Direct bank transfer</strong>
      </li>
    </ul>
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
        <p><span>&#128379;</span>0815220802</p>
        <p><span>&#9993;</span>honghieu2208@gmail.com</p>
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

<style lang="scss" scoped>
@import '@/assets/variables';

.wrapper {
  display: flex;
  flex-direction: column;
  gap: 3.5rem;
  .order-info {
    display: flex;
    .order-info-item {
      font-size: $--font-xs;
      display: flex;
      flex-direction: column;
      padding-right: 2.3rem;
      margin-right: 2.3rem;
      strong {
        font-size: $--font-base;
      }
      &:not(:last-child) {
        border-right: 1px dashed $--color-border;
      }
    }
  }
  .section-title {
    width: 100%;
    padding: 2.1rem;
    font-size: $--font-xl;
    font-weight: $--font-bold;
    border: 1px solid $--color-border;
  }
  .order-detail-content {
    margin-top: -0.1rem;
    font-size: $--font-base;
    color: $--primary-color-text;
    width: 100%;
    thead tr {
      border: 1px solid $--color-border;
    }
    th,
    td {
      padding: 1.1rem 1.6rem;
    }
    td {
      border: 1px solid $--color-border;
    }
    th {
      text-align: left;
      font-weight: $--font-bold;
    }
  }
  .custom-info-wp {
    display: flex;
    color: $--primary-color-text;
    flex-direction: column;
    margin-top: -1.1rem;
    font-size: $--font-base;
    padding: 1.6rem;
    border: 1px solid $--color-border;
    gap: 0.5rem;
  }
}
</style>
