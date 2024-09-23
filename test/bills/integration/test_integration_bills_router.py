from shared.database import Base
from test.conftest import client, engine


def test_list_bills_pay_and_receive():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    client.post(
        "/contas-a-pagar-e-receber",
        json={
            "descricao": "Aluguel",
            "valor": "100",
            "tipo": "PAGAR",
            "data_previsao": "2024-09-19",
        },
    )
    client.post(
        "/contas-a-pagar-e-receber",
        json={
            "descricao": "Salário",
            "valor": "5000",
            "tipo": "RECEBER",
            "data_previsao": "2024-09-19",
        },
    )
    response = client.get("/contas-a-pagar-e-receber")

    assert response.status_code == 200


def test_create_bills_pay_and_receive_with_fornecedor_is_none():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    account = {
        'data_baixa': None,
        'data_previsao': '2024-09-23',
        'descricao': 'Aula',
        'esta_baixada': False,
        'fornecedor': None,
        'id': 1,
        'tipo': 'PAGAR',
        'valor': '50.0000000000',
        'valor_baixa': None
    }
    account_copy = account.copy()
    account_copy["id"] = 1

    response = client.post("/contas-a-pagar-e-receber", json=account)

    assert response.status_code == 422


def test_update_bills_pay_and_receive_with_supplier_is_null():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    client.post(
        "/fornecedor-cliente",
        json={
            "nome": "Pedro",
        },
    )

    response = client.post(
        "/contas-a-pagar-e-receber",
        json={
            "descricao": "Curso de python",
            "valor": "333.0000000000",
            "tipo": "PAGAR",
            "data_previsao": "2024-09-19",
            "fornecedor": None,
        },
    )

    assert response.status_code == 422

def test_not_found_bills_pay_and_receive():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    response_put = client.get("/contas-a-pagar-e-receber/1")
    assert response_put.status_code == 404


def test_report_costs_expected_monthly_of_a_year():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    response = client.get("contas-a-pagar-e-receber/previsao_gastos_do_mes")
    assert response.status_code == 200
    assert len(response.json()) == 0

