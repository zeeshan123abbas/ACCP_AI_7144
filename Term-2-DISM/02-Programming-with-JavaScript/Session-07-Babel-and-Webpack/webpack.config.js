// webpack.config.js
const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = (env, argv) => {
  const isProd = argv.mode === "production";
  return {
    entry: "./src/index.js",
    output: {
      path: path.resolve(__dirname, "dist"),
      filename: isProd ? "[name].[contenthash].js" : "[name].js",
      clean: true // empty dist/ before each build
    },
    devtool: isProd ? "source-map" : "eval-source-map",
    module: {
      rules: [
        { test: /\.js$/, exclude: /node_modules/, use: "babel-loader" },
        { test: /\.css$/, use: ["style-loader", "css-loader"] }
      ]
    },
    plugins: [new HtmlWebpackPlugin({ template: "./src/index.html", title: "Webpack Demo" })],
    devServer: { static: "./dist", port: 8080, open: true, hot: true }
  };
};
