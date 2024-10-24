interface AuthToken {
  access: string;
  refresh: string;
}

interface DropdownItem {
  title: string;
  action: string;
}

interface OptionItem {
  image?: string;
  displayValue: string;
  value: string;
}

interface LoginItem {
  email: string;
  password: string;
}

interface RegisterItem {
  email: string;
  password: string;
  retypePassword: string;
}

interface SidebarItem {
  title: string;
  path: string;
  icon: string;
}

interface TabItem {
  title: string;
  path: string;
}

export {
  AuthToken,
  DropdownItem,
  OptionItem,
  LoginItem,
  RegisterItem,
  SidebarItem,
  TabItem,
};
