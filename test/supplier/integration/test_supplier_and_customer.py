from shared.database import Base
from test.conftest import client, engine


def test_list_bills_supplier_and_customer():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    client.post("/fornecedor-cliente", json={"nome": "Maria"})
    client.post("/fornecedor-cliente", json={"nome": "Pedro"})
    response = client.get("/fornecedor-cliente")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "nome": "Maria",
        },
        {"id": 2, "nome": "Pedro"},
    ]


def test_create_bill_supplier_and_customer():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    supplier = {
        "nome": "Pedro",
    }

    supplier_copy = supplier.copy()
    supplier_copy["id"] = 1

    response = client.post("/fornecedor-cliente", json=supplier)
    assert response.status_code == 201
    assert response.json() == supplier_copy


def test_error_in_supplier_name_amount():
    response = client.post(
        "/fornecedor-cliente",
        json={
            "nome": "012345678912345678912345678254154105641056410515415415419125",
        },
    )

    assert response.status_code == 201


def test_update_bill_supplier_and_customer():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    response = client.post("/fornecedor-cliente", json={"nome": "Pedrinho"})

    supplier_id = response.json()["id"]

    response_put = client.put(
        f"/fornecedor-cliente/{supplier_id}", json={"nome": "Maria"}
    )
    assert response_put.status_code == 200


def test_remove_supplier_and_customer():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    response = client.post("/fornecedor-cliente", json={"nome": "Pedrinho"})

    supplier_id = response.json()["id"]

    response_put = client.delete(f"/fornecedor-cliente/{supplier_id}")
    assert response_put.status_code == 204


def test_get_supplier_and_customer():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    response = client.post("/fornecedor-cliente", json={"nome": "Maria Eduarda"})

    supplier_id = response.json()["id"]

    response_put = client.get(f"/fornecedor-cliente/{supplier_id}")
    assert response_put.status_code == 200


def test_get_supplier_and_customer_not_found():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    response = client.get("/fornecedor-cliente/1")
    assert response.status_code == 404
