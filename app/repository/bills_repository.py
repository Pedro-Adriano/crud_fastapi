from sqlalchemy import extract

from app.models.bills_models import ContaPagarReceber
from app.models.enums import ContaPagarReceberTipoEnum


class BillsRepository:

    def list_bills_month_in_year(self, db, year):
        return (
            db.query(ContaPagarReceber)
            .filter(extract("year", ContaPagarReceber.data_previsao) == year)
            .filter(ContaPagarReceber.tipo == ContaPagarReceberTipoEnum.PAGAR)
            .order_by(ContaPagarReceber.data_previsao)
            .all()
        )

    def list_bills(self, db):
        return db.query(ContaPagarReceber).all()

    def list_bill_by_id(self, db, id):
        return db.query(ContaPagarReceber).get(id)

    def _valid_register_number(self, db, ano: int, mes: int) -> int:
        return (
            db.query(ContaPagarReceber)
            .filter(extract("year", ContaPagarReceber.data_previsao) == ano)
            .filter(extract("month", ContaPagarReceber.data_previsao) == mes)
            .count()
        )

    def _valid_supplier(self, conta_a_pagar_e_receber_request, db):
        if conta_a_pagar_e_receber_request.fornecedor_cliente_id:
            return db.query(conta_a_pagar_e_receber_request.fornecedor_cliente_id)

    def _create_bill(self, conta_a_pagar_e_receber_request, db):
        contas_a_pagar_e_receber = ContaPagarReceber(
            **conta_a_pagar_e_receber_request.model_dump()
        )

        db.add(contas_a_pagar_e_receber)
        db.commit()
        db.refresh(contas_a_pagar_e_receber)
        return contas_a_pagar_e_receber
