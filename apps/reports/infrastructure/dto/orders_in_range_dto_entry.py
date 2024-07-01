


from datetime import date
from pydantic import BaseModel


class OrdersInRangeDtoEntry (BaseModel):
    from_date: date
    to_date: date