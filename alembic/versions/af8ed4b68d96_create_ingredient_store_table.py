"""create_ingredient_store_table

Revision ID: af8ed4b68d96
Revises: 71f65961713f
Create Date: 2024-07-01 20:52:36.673143

"""
from uuid import uuid4
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

from db.db_base import table_exists

# revision identifiers, used by Alembic.
revision = 'af8ed4b68d96'
down_revision = '71f65961713f'
branch_labels = None
depends_on = None

def create_ingredient_store_table():
    if not table_exists("ingredient_store"):
        op.create_table(
            'ingredient_store',
            sa.Column('id', sa.String(),  primary_key=True, default=uuid4()),
            sa.Column('fk_ingredient', sa.String(), sa.ForeignKey('ingredient.id'), nullable=False),
            sa.Column('fk_store', sa.String(), sa.ForeignKey('store.id'), nullable=False),
            sa.Column('quantity', sa.Float, nullable=False)
        )

def upgrade() -> None:
    create_ingredient_store_table()


def downgrade() -> None:
    op.drop_table('ingredient_store')
