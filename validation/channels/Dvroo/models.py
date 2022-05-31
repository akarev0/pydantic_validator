from curses import beep
from typing import Optional, List
from pydantic import BaseModel, Field


class Image(BaseModel):
    url: str


class Translation(BaseModel):
    en: str


class TimePeriod(BaseModel):
    start: str
    end: str


class Schedule(BaseModel):
    day_of_week: int
    time_periods: List[TimePeriod] = Field(default_factory=list)


class Mealtime(BaseModel):
    id: str
    name: Translation
    description: Translation
    seo_description: Translation
    image: Image
    category_ids: List[str] = Field(default_factory=list)
    schedule: List[Schedule] = Field(default_factory=list)


class Category(BaseModel):
    id: str
    name: Translation
    description: Translation
    item_ids: List[str] = Field(default_factory=list)


class Override(BaseModel):
    type: str
    id: str
    price: int


class PriceInfo(BaseModel):
    price: int
    overrides: List[Override]


class KcalRange(BaseModel):
    low: int
    high: int


class NutritionalInfo(BaseModel):
    energy_kcal: KcalRange


class Item(BaseModel):
    id: str
    name: Translation
    description: Translation
    price_info: PriceInfo
    plu: str
    ian: str
    image: dict
    is_eligible_as_replacement: bool
    is_eligible_for_substitution: bool
    tax_rate: float
    modifier_ids: List[str] = Field(default_factory=list)
    allergies: List[str] = Field(default_factory=list)
    nutritional_info: NutritionalInfo
    contains_alcohol: bool
    max_quantity: int


class Modifier(BaseModel):
    id: str
    name: Translation
    description: Translation
    min_selection: int
    max_selection: int
    repeatable: bool
    item_ids: List[str] = Field(default_factory=list)


class Menu(BaseModel):
    """Inner menu."""

    mealtimes: List[Mealtime] = Field(default_factory=list)
    categories: List[Category] = Field(default_factory=list)
    items: List[Item] = Field(default_factory=list)
    modifiers: List[Modifier] = Field(default_factory=list)


class DVRoMenu(BaseModel):
    """Menu model."""

    name: Optional[str]
    menu: Menu
    site_ids: List[str] = Field(default_factory=list)
