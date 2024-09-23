from fastapi import APIRouter, Depends
from typing import List, Type
from sqlalchemy.orm import Session

from app.models.supplier_and_customer_models import FornecedorCliente
from shared.dependencies import get_db
from shared.exceptions import NotFound
from app.models.schema import FornecedorClienteResponse, FornecedorClienteRequest

router = APIRouter(prefix="/fornecedor-cliente")


@router.get("", response_model=List[FornecedorClienteResponse])
def listar_fornecedor_cliente(
    db: Session = Depends(get_db),
) -> list[Type[FornecedorClienteResponse]]:
    return db.query(FornecedorCliente).all()


@router.get("/{id_fornecedor}", response_model=FornecedorClienteResponse)
def listar_conta(
    id_fornecedor: int, db: Session = Depends(get_db)
) -> list[FornecedorClienteResponse]:
    fornecedor_cliente: FornecedorCliente = busca_fornecedor_cliente_por_id(
        id_fornecedor, db
    )

    return fornecedor_cliente


@router.post("", response_model=FornecedorClienteResponse, status_code=201)
def criar_fornecedor_cliente(
    conta_a_pagar_e_receber_request: FornecedorClienteRequest,
    db: Session = Depends(get_db),
) -> FornecedorClienteResponse:

    fornecedor_cliente = FornecedorCliente(
        **conta_a_pagar_e_receber_request.model_dump()
    )

    db.add(fornecedor_cliente)
    db.commit()
    db.refresh(fornecedor_cliente)

    return fornecedor_cliente


@router.put(
    "/{id_fornecedor}", response_model=FornecedorClienteResponse, status_code=200
)
def atualizar_fornecedor_cliente(
    id_fornecedor: int,
    fornecedor_e_cliente: FornecedorClienteRequest,
    db: Session = Depends(get_db),
) -> FornecedorClienteResponse:

    conta_a_receber: FornecedorCliente = busca_fornecedor_cliente_por_id(
        id_fornecedor, db
    )
    conta_a_receber.nome = fornecedor_e_cliente.nome

    db.add(conta_a_receber)
    db.commit()
    db.refresh(conta_a_receber)
    return conta_a_receber


@router.delete("/{id_fornecedor}", status_code=204)
def remover_fornecedor(
    id_fornecedor: int,
    db: Session = Depends(get_db),
) -> None:

    db.delete(busca_fornecedor_cliente_por_id(id_fornecedor, db))
    db.commit()


def busca_fornecedor_cliente_por_id(
    id_fornecedor: int, db: Session
) -> FornecedorCliente:
    fornecedor_e_cliente = db.query(FornecedorCliente).get(id_fornecedor)

    if not fornecedor_e_cliente:
        raise NotFound("Fornecedor e cliente")

    return fornecedor_e_cliente
