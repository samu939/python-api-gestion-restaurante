


from datetime import date
from pydantic import BaseModel


class GetSellsInRangeDto (BaseModel):
    begin: date
    end: date