"""ADD novas funções

Revision ID: 15c8353b7f1b
Revises: fc1ed09eae8b
Create Date: 2022-07-01 02:39:24.977352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15c8353b7f1b'
down_revision = 'fc1ed09eae8b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('senha', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.drop_column('senha')

    # ### end Alembic commands ###
