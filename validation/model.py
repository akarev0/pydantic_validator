from pydantic import (
    BaseModel,
    Field,
    validator,
    create_model_from_namedtuple,
)
from typing import List
from typing import NamedTuple


class ErrorData(NamedTuple):
    menuField: str
    itemIndex: int
    fieldName: str


ErrorLocationModel = create_model_from_namedtuple(ErrorData)


class PyValidationError(BaseModel):
    """Wrapper for Pydantic ValidationError."""

    errorInfo: tuple = Field(alias="loc")
    errorMessage: str = Field(alias="msg")
    type: str

    @validator("errorInfo")
    def _loc(cls, value):
        _menu, _index, _field = value
        return ErrorLocationModel(menuField=_menu, itemIndex=_index, fieldName=_field)

    class Config:
        validation_assignment = True


class ErrorSerializer(BaseModel):
    """Build a user-friendly errors list."""

    errors: List[PyValidationError]


class ChannelMenuCategory(BaseModel):
    id: str
    name: str

    @validator("name")
    def _length(cls, value):
        assert not value, "Name value is missed"
        assert (
            0 >= len(value) >= 50
        ), "Name length should be more that 0 and less than 50"


class ChannelMenuProduct(BaseModel):
    plu: str
    price: float

    @validator("plu")
    def _pluLength(cls, plu):
        assert not plu, "PLU is missed!"
        assert 0 <= len(plu) >= 50, "PLU length should be more that 0 and less than 50"

    @validator("price")
    def _priceValue(cls, price):
        assert price, "price is missed!"
        assert price <= 0, "price must be positive!"


class ChannelMenu(BaseModel):
    categories: List[ChannelMenuCategory]
    products: List[ChannelMenuProduct]
