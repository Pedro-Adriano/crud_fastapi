from collections import OrderedDict

from app.repository.bills_repository import BillsRepository

from fastapi import HTTPException
from sqlalchemy.orm import Session

from shared.exceptions import NotFound
from app.models.schema import (
    ContaPagarReceberRequest,
    PrevisaoPorMes,
)


class BillsService:

    def list_bills_month_in_year(self, db, year):
        accounts = BillsRepository().list_bills_month_in_year(db, year)

        month_value = OrderedDict()

        for account in accounts:
            month = account.data_previsao.month
            valor = account.valor

            if month_value.get(month) is None:
                month_value[month] = 0

            month_value[month] += valor
        return [PrevisaoPorMes(mes=k, valor_total=v) for k, v in month_value.items()]

    def list_bills(self, db):
        return BillsRepository().list_bills(db)

    def list_bill_by_id(self, db, id):
        conta_a_receber = BillsRepository().list_bill_by_id(db, id)

        if not conta_a_receber:
            raise NotFound("Conta a pagar e receber")

        return conta_a_receber

    def launch_excecao_when_ultrapass_number_of_records(
        self, conta_a_pagar_receber_request: ContaPagarReceberRequest, db: Session
    ) -> None:
        if (
            BillsRepository()._valid_register_number(
                db,
                conta_a_pagar_receber_request.data_previsao.year,
                conta_a_pagar_receber_request.data_previsao.month,
            )
            > 100
        ):
            raise HTTPException(
                status_code=422, detail="Você não pode lançar contas nesse mês"
            )

    def _valid_supplier(self, conta_a_pagar_e_receber_request, db):
        contas_a_pagar_e_receber = BillsRepository()._valid_supplier(
            conta_a_pagar_e_receber_request, db
        )

        if not contas_a_pagar_e_receber:
            raise HTTPException(status_code=422, detail="Fornecedor não cadastrado")

    def _create_bill(self, conta_a_pagar_e_receber_request, db):
        return BillsRepository()._create_bill(conta_a_pagar_e_receber_request, db)
