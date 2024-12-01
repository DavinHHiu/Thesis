<template>
  <page-body class="content">
    <Toast />
    <div class="product">
      <div class="product-image">
        <image-preview :images="currentSku?.images || []" />
      </div>
      <div class="product-desc">
        <nav class="breadcrumb">
          <a href="">Home</a>&nbsp;/&nbsp;<a href="">Men</a>&nbsp;/&nbsp;DNK
          Yellow Shoes
        </nav>
        <span class="single-product-category mb-[1.6rem] block"
          ><a href="" rel="tag" v-text="productDetail?.categories?.[0]"
        /></span>
        <h1 class="product-title mb-[1.5rem]" v-text="productDetail.name" />
        <p class="price py-[1.5rem] border-y">
          <!-- <del aria-hidden="true" class="mr-[10px] text-slate-400">$150.00</del> -->
          <span
            class="screen-reader-text font-bold"
            v-text="formatAmount(currentSku?.price)"
          />
          <!-- <span class="ast-shipping-text">+ Free Shipping</span> -->
        </p>
        <div class="my-[1.6rem]">
          <product-sku-picker
            :skus="productDetail?.skus"
            :current-sku="currentSku"
            @update:sku="changeSku"
          />
        </div>
        <div class="action-wrapper flex gap-[2rem] mb-[2rem]">
          <custom-button
            class="btn-add h-[4.5rem]"
            intent="primary"
            :disabled="loading"
            v-t="'inputLabel.common.addToCart'"
            @click="handleAddToCart"
          />
        </div>
        <div class="my-[1.6rem]">
          <span v-text="productDetail?.summary" />
        </div>
        <div class="product_meta border-t">
          <span class="posted_in block pt-[1rem] mb-[2rem]"
            >Category: <a href="" v-text="productDetail?.categories?.[0]"
          /></span>
        </div>
      </div>
    </div>
    <div class="product-details-wrapper">
      <ul class="tabs">
        <li
          v-for="(x, index) in ['Description', 'Reviews (0)']"
          :key="index"
          :class="{ active: index === currentTabIndex }"
          @click="handleChangeTab(index)"
        >
          {{ x }}
        </li>
      </ul>
      <div class="product-details">
        <div class="pb-[2rem]">
          <div>
            <h3 class="product-details-title font-bold">Product description</h3>
          </div>
          <div class="mb-[2rem]">
            <p v-text="productDetail?.description" />
          </div>
        </div>
        <div v-for="image in currentSku?.images?.slice(1)" class="w-full">
          <img :src="image" class="w-full" />
        </div>
      </div>
    </div>
    <related-product-list />
  </page-body>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import ImagePreview from "@/components/common/organisms/ImagePreview.vue";
import ProductSkuPicker from "@/components/common/organisms/ProductSkuPicker.vue";
import RelatedProductList from "@/components/common/organisms/RelatedProductList.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import { useCartStore } from "@/stores/cart";
import { useProductStore } from "@/stores/product";
import { useToastStore } from "@/stores/toast";
import { NewCartItem, ProductSkuDetail } from "@/types/worker";
import { formatCurrency } from "@/utils/currency";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";
import { useI18n } from "vue-i18n";

export default defineComponent({
  name: "ProductDetail",
  components: {
    CustomButton,
    ImagePreview,
    PageBody,
    ProductSkuPicker,
    RelatedProductList,
    TextField,
  },
  data() {
    return {
      loading: false,
      currentTabIndex: 0,
      currentSku: {} as ProductSkuDetail,
    };
  },
  computed: {
    ...mapState(useProductStore, ["productDetail"]),
    ...mapState(useCartStore, ["cart"]),
  },
  methods: {
    ...mapActions(useProductStore, ["retrieveProductDetail"]),
    ...mapActions(useCartStore, ["addToCart"]),
    ...mapActions(useToastStore, ["toast"]),
    formatCurrency,
    formatAmount(amount: number) {
      const { locale } = useI18n();
      return this.formatCurrency(locale.value, amount);
    },
    handleChangeTab(index: Number) {
      // this.currentTabIndex = index;
    },
    changeSku(sku: ProductSkuDetail) {
      this.currentSku = sku;
    },
    handleAddToCart() {
      this.loading = true;
      const payload = {
        cart_id: this.cart.id,
        product_sku_id: this.currentSku.id,
        quantity: 1,
      } as NewCartItem;
      this.addToCart(payload)
        .then(() => {
          this.loading = false;
          this.toast({
            theme: "success",
            message: "productDetailPage.messages.addToCart.success",
          });
        })
        .catch(() => {
          this.loading = false;
          this.toast({
            theme: "danger",
            message: "productDetailPage.messages.addToCart.fail",
          });
        });
    },
  },
  async mounted() {
    const productId = this.$route.params.id;
    await this.retrieveProductDetail(productId as string);
    this.currentSku = this.productDetail?.skus[0] as ProductSkuDetail;
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.content {
  display: flex;
  flex-direction: column;
  padding: 6rem 0;
  .product {
    display: flex;
    width: 100%;
    padding: 0 2rem;
    justify-content: space-between;
    .product-image {
      width: 60%;
      .zoomImg {
        width: 100%;
        height: 100%;
      }
    }
    .product-desc {
      width: 35%;
      .single-product-category {
        font-size: $--font-base;
      }
      .product-title {
        font-size: $--font-4xl;
        text-transform: uppercase;
        color: $--dark-gray;
      }
      .breadcrumb {
        color: $--gray-color-900;
        margin-bottom: 1.5rem;
      }
      .price {
        font-size: $--font-2xl;
      }
      .ast-shipping-text {
        font-size: $--font-base;
      }
      .action-wrapper {
        width: 100%;
        .input-quantity {
          width: 15%;
          height: 4rem;
        }
        .btn-add {
          width: 100%;
        }
      }
    }
  }
  .product-details-wrapper {
    width: 100%;
    padding: 3.2rem 2rem 0;
    margin-top: 3.2rem;
    .tabs {
      display: flex;
      border-top: 1px solid $--color-border;
      li {
        margin-right: 1.6rem;
        font-size: $--font-base;
        font-weight: $--font-bold;
        padding: 1.5rem 0;
        cursor: default;
      }
      .active {
        position: relative;
        &::before {
          position: absolute;
          top: 0;
          content: "";
          width: 100%;
          border-top: 3px solid $--black-color-800;
        }
      }
    }
    .product-details {
      padding: 5rem 0 7rem;
      .product-details-title {
        font-size: 2.6rem;
        margin-bottom: 2rem;
      }
      .image-widget-container {
        width: 50%;
        img {
          width: 100%;
          width: 100%;
        }
      }
      .elementor-widget-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 7rem 10rem 7rem;
        width: 50%;
        gap: 2rem;
        .elementor-widget-title {
          font-size: $--font-xl;
          font-weight: $--font-bold;
          line-height: 5rem;
        }
        .elementor-widget-body {
          font-size: $--font-base;
          line-height: 3rem;
        }
      }
    }
  }
}
</style>
