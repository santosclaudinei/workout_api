from typing import Annotated, Optional
from pydantic import UUID4, Field, PositiveFloat

from workut_api.categorias.schemas import CategoriaIn
from workut_api.centro_treinamento.schemas import CentroTreinamentoAtleta
from workut_api.contrib.schemas import BaseSchema, OutMixin


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='José', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example=33,)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=85)]
    altura: Annotated[PositiveFloat, Field(description='Peso do atleta', example=1.85)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]

class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass

class AtletaCreatedResponse(BaseSchema):
    id: UUID4

class AtletaPatch(BaseSchema):
    nome: Annotated[Optional[str], Field(description='Nome do atleta', example='José', max_length=50)]
    idade: Annotated[Optional[int], Field(description='Idade do atleta', example=33,)]
    peso: Annotated[Optional[PositiveFloat], Field(description='Peso do atleta', example=85)]
    altura: Annotated[Optional[PositiveFloat], Field(description='Peso do atleta', example=1.85)]
    sexo: Annotated[Optional[str], Field(description='Sexo do atleta', example='M', max_length=1)]

class AtletaGetAllResponse(BaseSchema):
    id: Annotated[UUID4, Field(description='Identificador do atleta')]
    nome: Annotated[str, Field(description='Nome do atleta', example='José', max_length=50)]
    centro_treinamento: CentroTreinamentoAtleta
    categoria: CategoriaIn