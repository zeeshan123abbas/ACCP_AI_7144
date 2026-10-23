// webpack.config.js
const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const { BundleAnalyzerPlugin } = require("webpack-bundle-analyzer");

module.exports = (env = {}) => ({
  mode: "production",
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "[name].[contenthash].js",
    chunkFilename: "[name].[contenthash].chunk.js",
    clean: true
  },
  optimization: {
    usedExports: true, // mark unused exports for tree shaking
    splitChunks: {
      chunks: "all",
      cacheGroups: {
        vendors: { test: /[\\/]node_modules[\\/]/, name: "vendors", priority: 10 }
      }
    }
  },
  plugins: [
    new HtmlWebpackPlugin({ title: "Code Splitting Demo" }),
    // run "npm run analyze" to open the treemap
    ...(env.analyze ? [new BundleAnalyzerPlugin()] : [])
  ]
});
