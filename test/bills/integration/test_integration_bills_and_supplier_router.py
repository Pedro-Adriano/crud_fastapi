from shared.database import Base
from test.conftest import client, engine

def test_register_mensal_limit():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    responses = []
    for item in range(0, 101):
        response = client.post(
            "/contas-a-pagar-e-receber",
            json={
                "descricao": "Salário",
                "valor": "1500",
                "tipo": "RECEBER",
                "fornecedor_cliente_id": 1,
                "data_previsao": "2024-09-19",
            },
        )

        responses.append(response)

    assert responses.pop().status_code == 201
    assert all([r.status_code == 201 for r in responses]) is True
