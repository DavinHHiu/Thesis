import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import Default from '@/layouts/Default.vue';
import AuthLayout from '@/layouts/AuthLayout.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: Default,
      children: [
        {
          path: '',
          name: 'home',
          component: HomeView
        }
      ]
    },
    {
      path: '/about',
      component: AuthLayout,
      children: [
        {
          path: '/about',
          name: 'about',
          component: () => import('@/views/AboutView.vue')
        }
      ]
    }
  ]
});

export default router;
