import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import LoginView from '@/views/LoginView.vue';
import RegisterView from '@/views/RegisterView.vue';
import AboutView from '@/views/AboutView.vue';
import CartView from '@/views/CartView.vue';
import ProductDetail from '@/views/ProductDetail.vue';
import SearchView from '@/views/SearchView.vue';
import CheckoutView from '@/views/CheckoutView.vue';
import OrderView from '@/views/OrderView.vue';
import CheckoutOrderView from '@/views/CheckoutOrderView.vue';
import CheckoutFormView from '@/views/CheckoutFormView.vue';

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
  ],
});

export default router;