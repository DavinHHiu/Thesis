import { createRouter, createWebHistory } from "vue-router";

const BaseView = () => import("@/views/BaseView.vue");
const ProductView = () => import("@/views/ProductView.vue");
const ProductUpdateView = () => import("@/views/ProductUpdateView.vue");
const ProductAttributeView = () => import("@/views/ProductAttributeView.vue");
const ProductAttributeUpdateView = () =>
  import("@/views/ProductAttributeUpdateView.vue");

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      component: BaseView,
      children: [
        {
          path: "products",
          children: [
            {
              path: "",
              component: ProductView,
            },
            {
              path: "add",
              component: ProductUpdateView,
            },
          ],
        },
        {
          path: "product-attributes",
          children: [
            {
              path: "",
              component: ProductAttributeView,
            },
            {
              path: "add",
              component: ProductAttributeUpdateView,
            },
            {
              path: "update/:id",
              name: "product.attributes.update",
              component: ProductAttributeUpdateView,
            },
          ],
        },
      ],
    },
  ],
});

export default router;
