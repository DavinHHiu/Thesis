from django.utils.translation import gettext_lazy as _

PAYMENT_METHOD_COD = "cod"
PAYMENT_METHOD_PAYPAL = "paypal"

PAYMENT_METHODS = (
    (PAYMENT_METHOD_COD, _("Cash on Delivery")),
    (PAYMENT_METHOD_PAYPAL, _("PayPal")),
)

SHIPMENT_METHOD_ECONOMY = "economy"
SHIPMENT_METHOD_FAST = "fast"
SHIPMENT_METHOD_EXPRESS = "express"

SHIPMENT_METHODS = (
    (SHIPMENT_METHOD_ECONOMY, _("Economy")),
    (SHIPMENT_METHOD_FAST, _("Fast")),
    (SHIPMENT_METHOD_EXPRESS, _("Express")),
)

ORDER_STATUS_PENDING = "pending"
ORDER_STATUS_COMFIRMED = "confirmed"
ORDER_STATUS_PROCESSING = "processing"
ORDER_STATUS_SHIPPING = "shipping"
ORDER_STATUS_DELIVERED = "delivered"
ORDER_STATUS_COMPLETED = "completed"
ORDER_STATUS_CANCELLED = "cancelled"
ORDER_STATUS_REFUNDED = "refunded"

ORDER_STATUSES = (
    (ORDER_STATUS_PENDING, _("Pending")),
    (ORDER_STATUS_COMFIRMED, _("Confirmed")),
    (ORDER_STATUS_PROCESSING, _("Processing")),
    (ORDER_STATUS_SHIPPING, _("Shipping")),
    (ORDER_STATUS_DELIVERED, _("Delivered")),
    (ORDER_STATUS_COMPLETED, _("Completed")),
    (ORDER_STATUS_CANCELLED, _("Cancelled")),
    (ORDER_STATUS_REFUNDED, _("Refunded")),
)
