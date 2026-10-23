import mongoose from "mongoose";

const productSchema = new mongoose.Schema(
  {
    name: { type: String, required: [true, "Name is required"], trim: true, maxlength: 100 },
    price: { type: Number, required: true, min: [0, "Price cannot be negative"] },
    category: { type: String, enum: ["mobile", "laptop", "accessory"], default: "accessory" },
    description: { type: String, default: "" },
    inStock: { type: Boolean, default: true },
  },
  { timestamps: true } // adds createdAt and updatedAt
);

export default mongoose.model("Product", productSchema);
