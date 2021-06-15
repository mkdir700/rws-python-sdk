# -*- coding: utf-8 -*-
import warnings

from .rws import RWS
from .apis import (
    Orders
)
# from .errors import MWSError
# from .apis import (
#     Feeds,
#     Finances,
#     InboundShipments,
#     Inventory,
#     MerchantFulfillment,
#     OffAmazonPayments,
#     Orders,
#     OutboundShipments,
#     Products,
#     Recommendations,
#     Reports,
#     Sellers,
#     Subscriptions,
#     EasyShip,
# )
# from .response import MWSResponse
# from .utils import types, DotDict

__all__ = [
    "Orders"
]

# __all__ = [
#     "EasyShip",
#     "Feeds",
#     "Finances",
#     "InboundShipments",
#     "Inventory",
#     "Marketplaces",
#     "MerchantFulfillment",
#     "MWS",
#     "MWSError",
#     "MWSResponse",
#     "OffAmazonPayments",
#     "Orders",
#     "OutboundShipments",
#     "Products",
#     "Recommendations",
#     "Reports",
#     "Sellers",
#     "Subscriptions",
#     "types",
#     "DotDict",
# ]

warnings.simplefilter("default")
