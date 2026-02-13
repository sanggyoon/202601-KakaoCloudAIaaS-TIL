interface Product {
  id: number;
  name: string;
  price: number;
  description?: string;
  category: string;
  inStock: boolean;
}

// 1. 상품 업데이트 DTO 타입 정의 (모든 필드 옵셔널, id 제외)
type UpdateProductDto = {
  id?: number;
  name?: string;
  price?: number;
  description?: string;
  category?: string;
  inStock?: boolean;
};

// 2. 완전한 상품 정보 타입 (모든 필드 필수)
type CompleteProduct = {
  id: number;
  name: string;
  price: number;
  description: string;
  category: string;
  inStock: boolean;
};

// 3. 업데이트 함수 구현
function updateProduct(id: number, updates: UpdateProductDto): Product {
  const existingProduct: Product = {
    id,
    name: 'Sample Product',
    price: 100,
    description: 'A sample product',
    category: 'General',
    inStock: true,
  };

  return { ...existingProduct, ...updates, id };
}

// 4. 상품 완성 함수 구현
function ensureComplete(product: Product): CompleteProduct {
  // 구현하세요 - description이 없으면 기본값 사용
  return {
    id: product.id,
    name: product.name,
    price: product.price,
    description: product.description ?? 'No description',
    category: product.category,
    inStock: product.inStock,
  };
}

// 테스트
const updated = updateProduct(1, { price: 29900 });
const complete = ensureComplete({
  id: 1,
  name: 'Item',
  price: 100,
  category: 'A',
  inStock: true,
});
