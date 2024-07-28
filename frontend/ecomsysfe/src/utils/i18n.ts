import { createI18n } from 'vue-i18n';
import en from '@/locales/en.yaml';
import vi from '@/locales/vi.yaml';

const messages = {
  en,
  vi,
};

const i18n = createI18n({
  locale: 'vi',
  fallbackLocale: 'en',
  messages,
});

export default i18n;
