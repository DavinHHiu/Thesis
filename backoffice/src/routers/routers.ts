import { createRouter, createWebHistory } from "vue-router";

const BaseView = () => import("@/views/BaseView.vue");
const Home = () => import("@/views/Home.vue");
const ProductView = () => import("@/views/ProductView.vue");

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      component: BaseView,
      children: [
        {
          path: "products",
          component: ProductView,
        },
      ],
    },
  ],
});

export default router;
