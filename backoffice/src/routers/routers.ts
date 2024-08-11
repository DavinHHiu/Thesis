import { createRouter, createWebHistory } from "vue-router";

const Home = () => import('@/views/Home.vue');
const ProductPage = () => import('@/views/ProductPage.vue');


const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: Home,
        },
        {
            path: '/products',
            component: ProductPage,
        }
    ]
});

export default router;