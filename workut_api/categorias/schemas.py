from pydantic import UUID4, Field
from sqlalchemy import String
from workut_api.contrib.schemas import BaseSchema
from typing import Annotated


class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description='Categoria do atleta', example='Scale', max_length=10)]

class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description='Identificador da categoria')]