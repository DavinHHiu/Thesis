import _ from "lodash";

const isLocalStorageAvailable = () => {
  try {
    const test = "test";
    localStorage.setItem(test, test);
    localStorage.removeItem(test);
    return true;
  } catch (e) {
    return false;
  }
};

export const get = (item: string) => {
  if (isLocalStorageAvailable()) {
    let value = localStorage.getItem(item);
    try {
      return JSON.parse(value as string);
    } catch {
      return value;
    }
  } else {
    alert("Can't get local storage item!");
  }
};

export const set = (item: string, value: string) => {
  if (isLocalStorageAvailable()) {
    localStorage.setItem(item, value);
  } else {
    alert("Can't set local storage item!");
  }
};

export const bulkSet = (item: object) => {
  if (isLocalStorageAvailable()) {
    _.forOwn(item, (value, key) => localStorage.setItem(key, value));
  } else {
    alert("Can't set local storage item!");
  }
};

export const remove = (item: string) => {
  if (isLocalStorageAvailable()) {
    localStorage.removeItem(item);
  } else {
    alert("Can't remove local storage item!");
  }
};

export const bulkRemove = (items: Array<string>) => {
  if (isLocalStorageAvailable()) {
    _.forEach(items, (item) => localStorage.removeItem(item));
  } else {
    alert("Can't remove local storage item!");
  }
};

const localStore = {
  get,
  set,
  bulkSet,
  remove,
  bulkRemove,
};

export default localStore;
