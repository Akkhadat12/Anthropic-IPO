import { defineConfig } from 'vite';
import { execSync } from 'node:child_process';

function sha() {
  if (process.env.VERCEL_GIT_COMMIT_SHA) return process.env.VERCEL_GIT_COMMIT_SHA.slice(0, 7);
  try {
    return execSync('git rev-parse --short HEAD').toString().trim();
  } catch {
    return 'local';
  }
}

export default defineConfig({
  define: {
    __BUILD_SHA__: JSON.stringify(sha()),
    __BUILD_DATE__: JSON.stringify(new Date().toISOString().slice(0, 10)),
  },
  build: { chunkSizeWarningLimit: 900 },
});
