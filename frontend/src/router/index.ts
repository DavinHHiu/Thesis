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
const PaymentSuccessView = () => import("@/views/PaymentSuccessView.vue");
const ProductDetail = () => import("@/views/ProductDetail.vue");
const ProfileView = () => import("@/views/ProfileView.vue");
const ProfileAddressView = () => import("@/views/ProfileAddressView.vue");
const ProfileLocaleSettingView = () =>
  import("@/views/ProfileLocaleSetting.vue");
const ProfileDetailView = () => import("@/views/ProfileDetailView.vue");
const ProfileChangePasswordView = () =>
  import("@/views/ProfileChangePasswordView.vue");
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
          name: "home",
          component: HomeView,
          meta: {
            intent: "second",
            requiresAuth: true,
          },
        },
        {
          path: "about",
          name: "about",
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
          path: "search/:query?",
          name: "search",
          component: SearchView,
          props: true,
        },
        {
          path: "checkout",
          component: CheckoutView,
          children: [
            {
              path: "order-form",
              name: "checkout-form",
              component: CheckoutFormView,
            },
            {
              path: "order-received/:orderId",
              name: "checkout-received",
              component: CheckoutOrderView,
            },
          ],
        },
        {
          path: "orders",
          name: "orderPage",
          component: OrderView,
        },
        {
          path: "profile",
          component: ProfileView,
          meta: {
            hasFooter: false,
            requiresAuth: true,
          },
          children: [
            {
              path: "",
              name: "profile.details",
              component: ProfileDetailView,
            },
            {
              path: "addresses",
              name: "profile.addresses",
              component: ProfileAddressView,
            },
            {
              path: "language",
              name: "profile.language",
              component: ProfileLocaleSettingView,
            },
            {
              path: "change-password",
              name: "profile.change-password",
              component: ProfileChangePasswordView,
            },
          ],
        },
      ],
    },
    {
      path: "/login",
      name: "login",
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
    {
      path: "/payment-success",
      component: PaymentSuccessView,
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    return { top: 0 };
  },
});

export default router;
