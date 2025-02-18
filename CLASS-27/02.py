from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    COMPLETED = 3

order_status = 1

if order_status == OrderStatus.PENDING.value:
    print("Pending")
elif order_status == OrderStatus.PROCESSING.value:
    print("Processing")
elif order_status == OrderStatus.COMPLETED.value:
    print("Completed")
else:
    print("no order")