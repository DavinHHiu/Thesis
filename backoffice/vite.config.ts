import VueI18nPlugin from "@intlify/unplugin-vue-i18n/vite";
import ViteYaml from "@modyfi/vite-plugin-yaml";
import vue from "@vitejs/plugin-vue";
import { resolve } from "node:path";
import { URL, fileURLToPath } from "node:url";
import { defineConfig } from "vite";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    VueI18nPlugin({
      strictMessage: false,
      include: resolve(__dirname, "**/locales/*.{yaml}"),
    }),
    ViteYaml(),
  ],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
});
