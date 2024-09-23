from datetime import date
from decimal import Decimal
from pydantic import BaseModel
from pydantic.v1 import Field
from app.models.enums import ContaPagarReceberTipoEnum


class FornecedorClienteResponse(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True


class FornecedorClienteRequest(BaseModel):
    nome: str = Field(min_lenght=3, max_lenght=255)


class ContaPagarReceberResponse(BaseModel):
    id: int
    descricao: str
    valor: Decimal
    tipo: str  # PAGAR, RECEBER
    data_previsao: date
    data_baixa: date | None = None
    valor_baixa: Decimal | None = None
    esta_baixada: bool | None = False
    fornecedor: FornecedorClienteResponse | None = None

    class Config:
        from_attributes = True


class ContaPagarReceberRequest(BaseModel):
    descricao: str = Field(min_lenght=3, max_lenght=30)
    valor: Decimal = Field(gt=0)
    tipo: ContaPagarReceberTipoEnum
    data_previsao: date
    fornecedor_cliente_id: int | None = None


class PrevisaoPorMes(BaseModel):
    mes: int
    valor_total: Decimal
