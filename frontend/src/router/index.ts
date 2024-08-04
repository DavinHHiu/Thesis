import { createRouter, createWebHistory } from 'vue-router';

import AboutView from '@/views/AboutView.vue';
import CartView from '@/views/CartView.vue';
import CheckoutFormView from '@/views/CheckoutFormView.vue';
import CheckoutOrderView from '@/views/CheckoutOrderView.vue';
import CheckoutView from '@/views/CheckoutView.vue';
import HomeView from '@/views/HomeView.vue';
import LoginView from '@/views/LoginView.vue';
import OrderView from '@/views/OrderView.vue';
import ProductDetail from '@/views/ProductDetail.vue';
import ProfileView from '@/views/ProfileView.vue';
import RegisterView from '@/views/RegisterView.vue';
import SearchView from '@/views/SearchView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: HomeView,
    },
    {
      path: '/about',
      component: AboutView,
    },
    {
      path: '/cart',
      component: CartView,
    },
    {
      path: '/login',
      component: LoginView,
    },
    {
      path: '/register',
      component: RegisterView,
    },
    {
      path: '/products/:id',
      component: ProductDetail,
      props: true,
    },
    {
      path: '/search/:query',
      component: SearchView,
      props: true,
    },
    {
      path: '/checkout',
      component: CheckoutView,
      children: [
        {
          path: 'order-form',
          component: CheckoutFormView,
        },
        {
          path: 'order-received',
          component: CheckoutOrderView,
        },
      ],
    },
    {
      path: '/orders',
      component: OrderView,
    },
    {
      path: '/profile',
      component: ProfileView,
    },
  ],
});

export default router;
