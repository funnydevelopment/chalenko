from typing import Union

from pydantic import BaseModel


class DatePrice(BaseModel):
    date: str
    price: Union[int, float]
