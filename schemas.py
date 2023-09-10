from typing import Union

from pydantic import BaseModel


class DatePrice(BaseModel):
    date: str
    price: Union[int, float]


class Date(BaseModel):
    date: str


class Price(BaseModel):
    price: Union[int, float]
