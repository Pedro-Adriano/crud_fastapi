from fastapi import Depends, APIRouter
from typing import List

from sqlalchemy.orm import Session

from app.models.bills_models import ContaPagarReceber
from app.routers.bills_router import (
    ContaPagarReceberResponse,
)
from app.services.supplier_and_customer_bills_service import SupplierCustomerBills
from shared.dependencies import get_db


router = APIRouter(prefix="/fornecedor-cliente")


@router.get(
    "/{id_fornecedor}/contas-a-pagar-e-receber",
    response_model=List[ContaPagarReceberResponse],
)
def get_all_bills_of_supplier(
    supplier_id: int, db: Session = Depends(get_db)
) -> list[ContaPagarReceber]:

    return SupplierCustomerBills().get_all_bills_of_supplier(supplier_id, db)
