"""chage prevision date type datetime to date

Revision ID: 947dcd234477
Revises: 3926d785f625
Create Date: 2024-09-19 22:05:55.304693

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '947dcd234477'
down_revision: Union[str, None] = '3926d785f625'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('alter table contas_a_pagar_e_receber alter column data_baixa type date')
    op.execute('alter table contas_a_pagar_e_receber alter column data_previsao type date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('alter table contas_a_pagar_e_receber alter column data_baixa type timestamp')
    op.execute('alter table contas_a_pagar_e_receber alter column data_previsao type timestamp')
    # ### end Alembic commands ###
