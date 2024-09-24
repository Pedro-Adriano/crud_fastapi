from app.models.bills_models import ContaPagarReceber
from app.repository.supplier_and_customer_bills_repository import SupplierCustomerBills


class SupplierCustomerBills:
    def __init__(self) -> None:
        self.repository = SupplierCustomerBills()

    def get_all_bills_of_supplier(self, supplier_id, db) -> list[ContaPagarReceber]:
        return self.repository.get_all_bills_of_supplier(supplier_id, db)
