from uuid import uuid4
from fastapi import APIRouter, Body, status, HTTPException
from pydantic import UUID4
from sqlalchemy import select

from workut_api.categorias.models import CategoriaModel
from workut_api.categorias.schemas import CategoriaIn, CategoriaOut
from workut_api.contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.post(
        '/',
        summary='Criar uma nova categoria',
        status_code=status.HTTP_201_CREATED,
        response_model=CategoriaOut
)

async def post(
    db_session: DatabaseDependency,
    categoria_in: CategoriaIn = Body(...)
) -> CategoriaOut:
    
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())

    db_session.add(categoria_model)
    await db_session.commit()

    return categoria_out.id

@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriaOut],
)
async def query(db_session: DatabaseDependency) -> list[CategoriaOut]:
    categorias: list[CategoriaOut] = (await db_session.execute(select(CategoriaModel))).scalars().all()

    return categorias

@router.get(
    '/{id}',
    summary='Consulta uma categoria pelo ID',
    status_code=status.HTTP_200_OK,
    response_model=CategoriaOut,
)
async def query(id: UUID4, db_session: DatabaseDependency) -> CategoriaOut:
    categoria: CategoriaOut = (
        await db_session.execute(select(CategoriaModel).filter_by(id=id))
    ).scalars().first()

    if not categoria:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f'Categoria não encontrada para o ID: {id}'
        )
    
    return categoria