interface ProductAttribute {
  id?: number;
  type: string;
  value: string;
}

interface DropdownItem {
  title: string;
  action: string;
}

interface OptionItem {
  displayValue: string;
  value: string;
}

export { DropdownItem, OptionItem, ProductAttribute };
