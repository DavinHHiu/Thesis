import './assets/main.scss';
import './assets/css/tailwind.css';

import { createApp } from 'vue';
import { createPinia } from 'pinia';
import i18n from '@/utils/i18n';

import App from './App.vue';
import router from './router';

const app = createApp(App);

app.use(createPinia());
app.use(i18n);
app.use(router);

app.mount('#app');