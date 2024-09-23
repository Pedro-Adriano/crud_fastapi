from datetime import datetime, date

from fastapi import APIRouter, Depends
from typing import List, Type
from sqlalchemy.orm import Session

from app.models.bills_models import ContaPagarReceber
from shared.dependencies import get_db
from shared.exceptions import NotFound
from app.models.schema import (
    ContaPagarReceberResponse,
    ContaPagarReceberRequest,
    PrevisaoPorMes,
)
from app.services.bills_service import BillsService

router = APIRouter(prefix="/contas-a-pagar-e-receber")


@router.get("/previsao_gastos_do_mes", response_model=List[PrevisaoPorMes])
def list_anual_bills_for_month(db: Session = Depends(get_db), ano=date.today().year):
    return BillsService().list_bills_month_in_year(db, ano)


@router.get("", response_model=List[ContaPagarReceberResponse])
def list_bills(db: Session = Depends(get_db)) -> list[Type[ContaPagarReceber]]:
    return BillsService().list_bills(db)


@router.get("/{id_conta}", response_model=ContaPagarReceberResponse)
def list_bill_by_id(
    id_conta: int, db: Session = Depends(get_db)
) -> list[ContaPagarReceber]:
    return BillsService().list_bill_by_id(db, id_conta)


@router.post("", response_model=ContaPagarReceberResponse, status_code=201)
def create_bill(
    conta_a_pagar_e_receber_request: ContaPagarReceberRequest,
    db: Session = Depends(get_db),
) -> ContaPagarReceberResponse:
    BillsService().launch_excecao_when_ultrapass_number_of_records(
        conta_a_pagar_e_receber_request, db
    )

    BillsService()._valid_supplier(conta_a_pagar_e_receber_request, db)

    return BillsService()._create_bill(conta_a_pagar_e_receber_request, db)


@router.put("/{id_conta}", response_model=ContaPagarReceberResponse, status_code=200)
def update_account(
    id_conta: int,
    conta_a_pagar_e_receber_request: ContaPagarReceberRequest,
    db: Session = Depends(get_db),
) -> ContaPagarReceberResponse:

    conta_a_receber: ContaPagarReceber = get_account_by_id(id_conta, db)
    conta_a_receber.tipo = conta_a_pagar_e_receber_request.tipo
    conta_a_receber.valor = conta_a_pagar_e_receber_request.valor
    conta_a_receber.descricao = conta_a_pagar_e_receber_request.descricao

    db.add(conta_a_receber)
    db.commit()
    db.refresh(conta_a_receber)

    return BillsService().list_bill_by_id(db, id_conta)


@router.post(
    "/{id_conta}/baixar", response_model=ContaPagarReceberResponse, status_code=200
)
def down_bill(
    id_conta: int,
    db: Session = Depends(get_db),
) -> ContaPagarReceberResponse:

    conta_a_receber: ContaPagarReceber = get_account_by_id(id_conta, db)

    if (
        not conta_a_receber.esta_baixada
        and conta_a_receber.valor != conta_a_receber.valor_baixa
    ):
        conta_a_receber.data_baixa = datetime.now()
        conta_a_receber.esta_baixada = True
        conta_a_receber.valor_baixa = conta_a_receber.valor

        db.add(conta_a_receber)
        db.commit()
        db.refresh(conta_a_receber)
    return conta_a_receber


@router.delete("/{id_conta}", status_code=204)
def remove_bill(
    id_conta: int,
    db: Session = Depends(get_db),
) -> None:

    db.delete(get_account_by_id(id_conta, db))
    db.commit()


def get_account_by_id(id_conta: int, db: Session) -> ContaPagarReceber:
    conta_a_receber = db.query(ContaPagarReceber).get(id_conta)

    if not conta_a_receber:
        raise NotFound("Conta a pagar e receber")

    return conta_a_receber
