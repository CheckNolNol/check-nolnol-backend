from humps import camel
from pydantic import BaseModel as PydanticBaseModel


def to_camel(x):
    return camel.case(x)


class BaseDTO(PydanticBaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
