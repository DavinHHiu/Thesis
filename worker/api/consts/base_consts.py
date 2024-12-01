from django.utils.translation import gettext_lazy as _

PAYMENT_METHOD_COD = "cod"
PAYMENT_METHOD_PAYPAL = "paypal"

PAYMENT_METHODS = (
    (PAYMENT_METHOD_COD, _("Cash on Delivery")),
    (PAYMENT_METHOD_PAYPAL, _("PayPal")),
)

PAYMENT_STATUS_PENDING = "pending"
PAYMENT_STATUS_SUCCESS = "success"
PAYMENT_STATUS_FAIL = "fail"
PAYMENT_STATUS_REFUND = "refund"

PAYMENT_STATUSES = (
    (PAYMENT_STATUS_PENDING, _("Pending")),
    (PAYMENT_STATUS_SUCCESS, _("Success")),
    (PAYMENT_STATUS_FAIL, _("Fail")),
    (PAYMENT_STATUS_REFUND, _("Refund")),
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

CLASS_LABEL_JEAN = "jean"
CLASS_LABEL_DRESS = "dress"
CLASS_LABEL_SWEATSHIRT = "sweatshirt"
CLASS_LABEL_BAG = "bag"
CLASS_LABEL_HAT = "hat"
CLASS_LABEL_T_SHIRT = "t-shirt"
CLASS_LABEL_SHORT = "short"
CLASS_LABEL_FLIP_FLOPS = "flip-flops"
CLASS_LABEL_BRA = "bra"
CLASS_LABEL_SHIRT = "shirt"
CLASS_LABEL_SHOES = "shoes"
CLASS_LABEL_BELT = "belt"
CLASS_LABEL_BLAZER = "blazer"
CLASS_LABEL_SKIRT = "skirt"
CLASS_LABEL_JACKET = "jacket"

CLASS_LABELS = (
    (CLASS_LABEL_JEAN, _("Jean")),
    (CLASS_LABEL_DRESS, _("Dress")),
    (CLASS_LABEL_SWEATSHIRT, _("Sweatshirt")),
    (CLASS_LABEL_BAG, _("Bag")),
    (CLASS_LABEL_HAT, _("Hat")),
    (CLASS_LABEL_T_SHIRT, _("T-Shirt")),
    (CLASS_LABEL_SHORT, _("Short")),
    (CLASS_LABEL_FLIP_FLOPS, _("Flip-Flops")),
    (CLASS_LABEL_BRA, _("Bra")),
    (CLASS_LABEL_SHIRT, _("Shirt")),
    (CLASS_LABEL_SHOES, _("Shoes")),
    (CLASS_LABEL_BELT, _("Belt")),
    (CLASS_LABEL_BLAZER, _("Blazer")),
    (CLASS_LABEL_SKIRT, _("Skirt")),
    (CLASS_LABEL_JACKET, _("Jacket")),
)
