<template>
  <div class="wrapper" :class="{ 'fade-out': isFading }">
    <div class="content-wrapper">
      <icon-check class="icon-check" height="15rem" width="15rem" />
      <span class="notify-text" v-t="'checkoutPage.message.success'" />
    </div>
  </div>
</template>

<script lang="ts">
import IconCheck from "@/components/icons/IconCheck.vue";
import { useOrderStore } from "@/stores/order";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "PaymentSuccessView",
  components: {
    IconCheck,
  },
  data() {
    return {
      token: "" as string,
      PayerID: "" as string,
      isFading: false,
    };
  },
  computed: {
    ...mapState(useOrderStore, ["order"]),
  },
  methods: {
    ...mapActions(useOrderStore, ["executePayment"]),
  },
  beforeMount() {
    this.token = this.$route.query.token as string;
    this.PayerID = this.$route.query.PayerID as string;

    const url = new URL(window.location.href);
    url.searchParams.delete("token");
    url.searchParams.delete("PayerID");

    window.history.replaceState({}, document.title, url.toString());
  },
  async mounted() {
    const response = await this.executePayment(this.token, this.PayerID);
    if (response.status === 200) {
      this.isFading = true;
      setTimeout(() => {
        this.$router.push({
          name: "checkout-received",
          params: {
            orderId: this.token,
          },
        });
      }, 300);
    }
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  opacity: 1;
  background-color: $--second-color;
  transition: all 0.3s ease-in-out;

  .content-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    .icon-check {
      animation: bounce 0.75s ease-in-out forwards;
    }
    .notify-text {
      font-size: 2rem;
      color: $--color-green;
      font-weight: $--font-bold;
      opacity: 0;
      animation: fadeIn 0.5s ease-in-out forwards;
      animation-delay: 0.75s;
    }
  }
  &.fade-out {
    opacity: 0;

    .content-wrapper {
      animation: zoomOut 0.5s ease-in-out;
    }
  }
}

@keyframes bounce {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.5);
  }
  100% {
    transform: scale(1);
  }
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 100%;
  }
}

@keyframes zoomOut {
  0% {
    transform: scale(1);
  }
  100% {
    transform: scale(0);
  }
}
</style>
