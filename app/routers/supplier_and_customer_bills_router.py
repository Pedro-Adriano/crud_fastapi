from fastapi import Depends, APIRouter
from typing import List, Type

from sqlalchemy.orm import Session

from app.models.bills_models import ContaPagarReceber
from app.routers.bills_router import (
    ContaPagarReceberResponse,
)
from shared.dependencies import get_db


router = APIRouter(prefix="/fornecedor-cliente")


@router.get(
    "/{id_fornecedor}/contas-a-pagar-e-receber",
    response_model=List[ContaPagarReceberResponse],
)
def get_all_bills_of_supplier(
    id_fornecedor: int, db: Session = Depends(get_db)
) -> list[Type[ContaPagarReceber]]:

    return (
        db.query(ContaPagarReceber).filter_by(fornecedor_cliente_id=id_fornecedor).all()
    )
