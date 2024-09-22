interface User {
  id?: string;
  avatar?: File | string;
  email: string;
  first_name?: string;
  last_name?: string;
  password?: string;
  birth_of_date?: Date;
  tel?: string;
}

interface Category {
  id?: number;
  name: string;
  description: string;
  created_at?: Date;
  updated_at?: Date;
}

interface SubCategory {
  id?: number;
  name: string;
  description: string;
  category: Category;
}

interface ProductAttribute {
  id?: number;
  type: string;
  value: string;
}

interface Product {
  id?: string;
  name: string;
  description?: string;
  summary?: string;
  rating?: number;
  categories: SubCategory[];
}

interface ProductSku {
  id?: string;
  size: ProductAttribute;
  color: ProductAttribute;
  images: File[];
  sku: string;
  price: number;
  quantity: number;
  product_id?: string;
}

interface ProductImage {
  image: File[];
}

interface ProductDetails {
  id?: string;
  name: string;
  description?: string;
  summary?: string;
  rating?: number;
  categories: SubCategory[];
  skus: ProductSku[];
}

export {
  Category,
  Product,
  ProductImage,
  ProductSku,
  ProductAttribute,
  ProductDetails,
  SubCategory,
  User,
};
