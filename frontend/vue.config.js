const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false, // Disable ESLint during build
  devServer: {
    proxy: {
      '/users': {
        target: 'http://localhost:8000', // Django server URL for user endpoints
        changeOrigin: true,
      },
    }
  },
});