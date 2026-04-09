import { defineConfig } from 'tsup'

export default defineConfig({
  entry: { app: 'src/main.ts' },
  format: ['esm'],
  outDir: 'dist',
  clean: true,
  bundle: true,
  splitting: false,
  dts: false,
  platform: 'node',
  target: 'es2024',
  minify: true,
  tsconfig: 'tsconfig.json',
  sourcemap: true,
})
