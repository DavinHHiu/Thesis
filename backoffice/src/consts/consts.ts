import i18n from "@/utils/i18n";

const apiVersion = "v1";
const APP_URL = `http://localhost:8000/api/${apiVersion}`;
const BASE_URL = `http://localhost:8000/api/${apiVersion}/bo`;

const ALL_STATUS = "all";

const ORDER_STATUS_PENDING = "pending";
const ORDER_STATUS_COMFIRMED = "confirmed";
const ORDER_STATUS_PROCESSING = "processing";
const ORDER_STATUS_SHIPPING = "shipping";
const ORDER_STATUS_DELIVERED = "delivered";
const ORDER_STATUS_COMPLETED = "completed";
const ORDER_STATUS_CANCELLED = "cancelled";
const ORDER_STATUS_REFUNDED = "refunded";

const ORDER_STATUSES = [
  ORDER_STATUS_PENDING,
  ORDER_STATUS_COMFIRMED,
  ORDER_STATUS_PROCESSING,
  ORDER_STATUS_SHIPPING,
  ORDER_STATUS_DELIVERED,
  ORDER_STATUS_COMPLETED,
  ORDER_STATUS_REFUNDED,
  ORDER_STATUS_CANCELLED,
];

const CHANGABLE_ORDER_STATUSES = [
  ORDER_STATUS_COMFIRMED,
  ORDER_STATUS_PROCESSING,
  ORDER_STATUS_SHIPPING,
  ORDER_STATUS_COMPLETED,
];

const ORDER_STATUS_MAP_COLOR = {
  pending: "#f58700",
  confirmed: "#00bd5ecc",
  processing: "#00bd5e80",
  shipping: "#0084d6aa",
  delivered: "#0084d6",
  completed: "#00bd5e",
  cancelled: "#ff0000",
  refunded: "#ff000080",
};

export type StatusType = keyof typeof consts.ORDER_STATUS_MAP_COLOR;

const STATISTIC_WEEK_PERIOD = "week";
const STATISTIC_MONTH_PERIOD = "month";
const STATISTIC_YEAR_PERIOD = "year";

const STATISTIC_PERIODS = [
  STATISTIC_WEEK_PERIOD,
  STATISTIC_MONTH_PERIOD,
  STATISTIC_YEAR_PERIOD,
];

const STATISTIC_PERIODS_DISPLAY = {
  [STATISTIC_WEEK_PERIOD]: i18n.global.t(
    "dashboardPage.statistics.period.week"
  ),
  [STATISTIC_MONTH_PERIOD]: i18n.global.t(
    "dashboardPage.statistics.period.month"
  ),
  [STATISTIC_YEAR_PERIOD]: i18n.global.t(
    "dashboardPage.statistics.period.year"
  ),
};

export type StatisticPeriodType = keyof typeof STATISTIC_PERIODS_DISPLAY;

const consts = {
  APP_URL,
  BASE_URL,
  ALL_STATUS,
  ORDER_STATUS_PENDING,
  ORDER_STATUS_COMFIRMED,
  ORDER_STATUS_PROCESSING,
  ORDER_STATUS_SHIPPING,
  ORDER_STATUS_DELIVERED,
  ORDER_STATUS_COMPLETED,
  ORDER_STATUS_CANCELLED,
  ORDER_STATUS_REFUNDED,
  ORDER_STATUS_MAP_COLOR,
  ORDER_STATUSES,
  CHANGABLE_ORDER_STATUSES,
  STATISTIC_WEEK_PERIOD,
  STATISTIC_MONTH_PERIOD,
  STATISTIC_YEAR_PERIOD,
  STATISTIC_PERIODS,
  STATISTIC_PERIODS_DISPLAY,
};

export default consts;
