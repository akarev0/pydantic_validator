from typing import Union
from pydantic import BaseModel, ValidationError
from .model import ErrorSerializer


class MenuValidator:
    @classmethod
    def validate(cls, model: BaseModel, menuData: dict) -> dict:
        try:
            menu = model.parse_obj(menuData)
            return menu.dict()
        except ValidationError as e:
            errors = {"errors": e.errors()}
            r = ErrorSerializer.parse_obj(errors)
            return r.dict()
