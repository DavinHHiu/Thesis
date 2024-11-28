// vite.config.ts
import VueI18nPlugin from "file:///D:/DoAnTotNghiep/backoffice/node_modules/@intlify/unplugin-vue-i18n/lib/vite.mjs";
import ViteYaml from "file:///D:/DoAnTotNghiep/backoffice/node_modules/@modyfi/vite-plugin-yaml/dist/index.js";
import vue from "file:///D:/DoAnTotNghiep/backoffice/node_modules/@vitejs/plugin-vue/dist/index.mjs";
import { resolve } from "node:path";
import { URL, fileURLToPath } from "node:url";
import { defineConfig } from "file:///D:/DoAnTotNghiep/backoffice/node_modules/vite/dist/node/index.js";
var __vite_injected_original_dirname = "D:\\DoAnTotNghiep\\backoffice";
var __vite_injected_original_import_meta_url = "file:///D:/DoAnTotNghiep/backoffice/vite.config.ts";
var vite_config_default = defineConfig({
  plugins: [
    vue(),
    VueI18nPlugin({
      strictMessage: false,
      include: resolve(__vite_injected_original_dirname, "**/locales/*.{yaml}")
    }),
    ViteYaml()
  ],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", __vite_injected_original_import_meta_url))
    }
  }
});
export {
  vite_config_default as default
};
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsidml0ZS5jb25maWcudHMiXSwKICAic291cmNlc0NvbnRlbnQiOiBbImNvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9kaXJuYW1lID0gXCJEOlxcXFxEb0FuVG90TmdoaWVwXFxcXGJhY2tvZmZpY2VcIjtjb25zdCBfX3ZpdGVfaW5qZWN0ZWRfb3JpZ2luYWxfZmlsZW5hbWUgPSBcIkQ6XFxcXERvQW5Ub3ROZ2hpZXBcXFxcYmFja29mZmljZVxcXFx2aXRlLmNvbmZpZy50c1wiO2NvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9pbXBvcnRfbWV0YV91cmwgPSBcImZpbGU6Ly8vRDovRG9BblRvdE5naGllcC9iYWNrb2ZmaWNlL3ZpdGUuY29uZmlnLnRzXCI7aW1wb3J0IFZ1ZUkxOG5QbHVnaW4gZnJvbSBcIkBpbnRsaWZ5L3VucGx1Z2luLXZ1ZS1pMThuL3ZpdGVcIjtcbmltcG9ydCBWaXRlWWFtbCBmcm9tIFwiQG1vZHlmaS92aXRlLXBsdWdpbi15YW1sXCI7XG5pbXBvcnQgdnVlIGZyb20gXCJAdml0ZWpzL3BsdWdpbi12dWVcIjtcbmltcG9ydCB7IHJlc29sdmUgfSBmcm9tIFwibm9kZTpwYXRoXCI7XG5pbXBvcnQgeyBVUkwsIGZpbGVVUkxUb1BhdGggfSBmcm9tIFwibm9kZTp1cmxcIjtcbmltcG9ydCB7IGRlZmluZUNvbmZpZyB9IGZyb20gXCJ2aXRlXCI7XG5cbi8vIGh0dHBzOi8vdml0ZWpzLmRldi9jb25maWcvXG5leHBvcnQgZGVmYXVsdCBkZWZpbmVDb25maWcoe1xuICBwbHVnaW5zOiBbXG4gICAgdnVlKCksXG4gICAgVnVlSTE4blBsdWdpbih7XG4gICAgICBzdHJpY3RNZXNzYWdlOiBmYWxzZSxcbiAgICAgIGluY2x1ZGU6IHJlc29sdmUoX19kaXJuYW1lLCBcIioqL2xvY2FsZXMvKi57eWFtbH1cIiksXG4gICAgfSksXG4gICAgVml0ZVlhbWwoKSxcbiAgXSxcbiAgcmVzb2x2ZToge1xuICAgIGFsaWFzOiB7XG4gICAgICBcIkBcIjogZmlsZVVSTFRvUGF0aChuZXcgVVJMKFwiLi9zcmNcIiwgaW1wb3J0Lm1ldGEudXJsKSksXG4gICAgfSxcbiAgfSxcbn0pO1xuIl0sCiAgIm1hcHBpbmdzIjogIjtBQUF5USxPQUFPLG1CQUFtQjtBQUNuUyxPQUFPLGNBQWM7QUFDckIsT0FBTyxTQUFTO0FBQ2hCLFNBQVMsZUFBZTtBQUN4QixTQUFTLEtBQUsscUJBQXFCO0FBQ25DLFNBQVMsb0JBQW9CO0FBTDdCLElBQU0sbUNBQW1DO0FBQTBILElBQU0sMkNBQTJDO0FBUXBOLElBQU8sc0JBQVEsYUFBYTtBQUFBLEVBQzFCLFNBQVM7QUFBQSxJQUNQLElBQUk7QUFBQSxJQUNKLGNBQWM7QUFBQSxNQUNaLGVBQWU7QUFBQSxNQUNmLFNBQVMsUUFBUSxrQ0FBVyxxQkFBcUI7QUFBQSxJQUNuRCxDQUFDO0FBQUEsSUFDRCxTQUFTO0FBQUEsRUFDWDtBQUFBLEVBQ0EsU0FBUztBQUFBLElBQ1AsT0FBTztBQUFBLE1BQ0wsS0FBSyxjQUFjLElBQUksSUFBSSxTQUFTLHdDQUFlLENBQUM7QUFBQSxJQUN0RDtBQUFBLEVBQ0Y7QUFDRixDQUFDOyIsCiAgIm5hbWVzIjogW10KfQo=
