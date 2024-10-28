import { createRouter, createWebHistory } from "vue-router";

const AboutView = () => import("@/views/AboutView.vue");
const BaseView = () => import("@/views/BaseView.vue");
const CartView = () => import("@/views/CartView.vue");
const CheckoutFormView = () => import("@/views/CheckoutFormView.vue");
const CheckoutOrderView = () => import("@/views/CheckoutOrderView.vue");
const CheckoutView = () => import("@/views/CheckoutView.vue");
const HomeView = () => import("@/views/HomeView.vue");
const LoginView = () => import("@/views/LoginView.vue");
const OrderView = () => import("@/views/OrderView.vue");
const ProductDetail = () => import("@/views/ProductDetail.vue");
const ProfileView = () => import("@/views/ProfileView.vue");
const RegisterView = () => import("@/views/RegisterView.vue");
const SearchView = () => import("@/views/SearchView.vue");

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      component: BaseView,
      children: [
        {
          path: "",
          component: HomeView,
          meta: {
            intent: "second",
            requiresAuth: true,
          },
        },
        {
          path: "about",
          component: AboutView,
        },
        {
          path: "cart",
          name: "cartPage",
          component: CartView,
        },
        {
          path: "products/:id",
          name: "product.detail",
          component: ProductDetail,
          props: true,
        },
        {
          path: "search/:query",
          component: SearchView,
          props: true,
        },
        {
          path: "checkout",
          component: CheckoutView,
          children: [
            {
              path: "order-form",
              component: CheckoutFormView,
            },
            {
              path: "order-received",
              component: CheckoutOrderView,
            },
          ],
        },
        {
          path: "orders",
          component: OrderView,
        },
        {
          path: "profile",
          component: ProfileView,
          meta: {
            requiresAuth: true,
          },
        },
      ],
    },
    {
      path: "/login",
      component: LoginView,
      meta: {
        requiresAuth: false,
      },
    },
    {
      path: "/register",
      name: "register",
      component: RegisterView,
      meta: {
        requiresAuth: false,
      },
    },
  ],
});

export default router;
