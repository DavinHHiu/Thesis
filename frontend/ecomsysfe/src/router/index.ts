import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import LoginView from '@/views/LoginView.vue';
import RegisterView from '@/views/RegisterView.vue';
import AboutView from '@/views/AboutView.vue';
import CartView from '@/views/CartView.vue';
import ProductDetail from '@/views/ProductDetail.vue';
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
  ],
});

export default router;
