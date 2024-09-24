from app.models.bills_models import ContaPagarReceber


class SupplierCustomerBills:
    def get_all_bills_of_supplier(self, supplier_id, db) -> list[ContaPagarReceber]:
        return (
            db.query(ContaPagarReceber)
            .filter_by(fornecedor_cliente_id=supplier_id)
            .all()
        )
