import { defineConfig } from 'vite'
import { ViteMinifyPlugin } from 'vite-plugin-minify'

export default defineConfig({
  base: '/portfolio/',
  plugins: [
    ViteMinifyPlugin({})
  ],
  build: {
    rollupOptions: {
      input: {
        main: 'index.html',
        pekos: 'pekos-case-study.html',
        sop: 'sop-case-study.html'
      },
      output: {
        assetFileNames: 'assets/[name]-[hash][extname]',
        chunkFileNames: 'assets/[name]-[hash].js',
        entryFileNames: 'assets/[name]-[hash].js',
      },
    },
  },
})