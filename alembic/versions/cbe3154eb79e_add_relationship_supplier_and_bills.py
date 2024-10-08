"""add relationship supplier and bills

Revision ID: cbe3154eb79e
Revises: bc19d6302ec4
Create Date: 2024-09-17 21:36:30.228674

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "cbe3154eb79e"
down_revision: Union[str, None] = "bc19d6302ec4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "contas_a_pagar_e_receber",
        sa.Column("fornecedor_cliente_id", sa.Integer(), nullable=True),
    )
    op.create_foreign_key(
        None,
        "contas_a_pagar_e_receber",
        "fornecedor_cliente",
        ["fornecedor_cliente_id"],
        ["id"],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "contas_a_pagar_e_receber", type_="foreignkey")
    op.drop_column("contas_a_pagar_e_receber", "fornecedor_cliente_id")
    # ### end Alembic commands ###
