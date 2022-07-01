"""Inicial

Revision ID: 40c59cbcec0f
Revises: 
Create Date: 2022-07-01 00:03:32.157034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40c59cbcec0f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pedido',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=True),
    sa.Column('entrega', sa.Boolean(), nullable=True),
    sa.Column('endereco', sa.String(), nullable=True),
    sa.Column('observacoes', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pedido_id'), 'pedido', ['id'], unique=False)
    op.create_table('produto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('detalhes', sa.String(), nullable=True),
    sa.Column('preco', sa.Float(), nullable=True),
    sa.Column('disponivel', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_produto_id'), 'produto', ['id'], unique=False)
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('telefone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('telefone')
    )
    op.create_index(op.f('ix_usuario_id'), 'usuario', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_usuario_id'), table_name='usuario')
    op.drop_table('usuario')
    op.drop_index(op.f('ix_produto_id'), table_name='produto')
    op.drop_table('produto')
    op.drop_index(op.f('ix_pedido_id'), table_name='pedido')
    op.drop_table('pedido')
    # ### end Alembic commands ###
