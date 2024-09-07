import { URL, fileURLToPath } from 'node:url';

import ViteYaml from '@modyfi/vite-plugin-yaml';
import VueI18nPlugin from '@intlify/unplugin-vue-i18n/vite';
import { defineConfig } from 'vite';
import { resolve } from 'node:path';
import vue from '@vitejs/plugin-vue';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    VueI18nPlugin({
      strictMessage: false,
      include: resolve(__dirname, '**/locales/*.{yaml}'),
    }),
    ViteYaml(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
});
