const apiVersion = "v1";
const APP_URL = `http://localhost:8000/api/${apiVersion}`;
const BASE_URL = `http://localhost:8000/api/${apiVersion}/eu`;

const ALL_STATUS = "all";

const ORDER_STATUS_PENDING = "pending";
const ORDER_STATUS_COMFIRMED = "confirmed";
const ORDER_STATUS_PROCESSING = "processing";
const ORDER_STATUS_SHIPPING = "shipping";
const ORDER_STATUS_DELIVERED = "delivered";
const ORDER_STATUS_COMPLETED = "completed";
const ORDER_STATUS_CANCELLED = "cancelled";
const ORDER_STATUS_REFUNDED = "refunded";

const ORDER_STATUSES = {
  pending: "#f58700",
  confirmed: "#00bd5ecc",
  processing: "#00bd5e80",
  shipping: "#0084d6aa",
  delivered: "#0084d6",
  completed: "#00bd5e",
  cancelled: "#ff0000",
  refunded: "#ff000080",
};

type StatusType = keyof typeof consts.ORDER_STATUSES;

const consts = {
  ALL_STATUS,
  APP_URL,
  BASE_URL,
  ORDER_STATUS_PENDING,
  ORDER_STATUS_COMFIRMED,
  ORDER_STATUS_PROCESSING,
  ORDER_STATUS_SHIPPING,
  ORDER_STATUS_DELIVERED,
  ORDER_STATUS_COMPLETED,
  ORDER_STATUS_CANCELLED,
  ORDER_STATUS_REFUNDED,
  ORDER_STATUSES,
};

export default consts;

export { StatusType };
