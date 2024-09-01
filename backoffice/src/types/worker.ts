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

interface Address {
  id?: number;
  user: User;
  title: string;
  address_1: string;
  address_2?: string;
  zipcode?: string;
  tel: string;
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
  cover?: File | string;
  categories: SubCategory[];
  size: ProductAttribute;
  color: ProductAttribute;
  sku: string;
  price: number;
  quantity: number;
}

export { Address, Category, Product, ProductAttribute, SubCategory, User };
