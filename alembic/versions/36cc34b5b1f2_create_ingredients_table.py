"""create_ingredients_and_store_tables

Revision ID: 36cc34b5b1f2
Revises: 492eec39b72d
Create Date: 2024-07-01 20:46:36.514100

"""
from uuid import uuid4
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

from db.db_base import table_exists


# revision identifiers, used by Alembic.
revision = '36cc34b5b1f2'
down_revision = '492eec39b72d'
branch_labels = None
depends_on = None



def create__ingredients_table():
    if not table_exists("ingredient"):
        op.create_table("ingredient", 
                    sa.Column("id", sa.String(),  primary_key=True, default=uuid4()),
                    sa.Column("name", sa.String(40), index=True, nullable=False))


def upgrade() -> None:
    create__ingredients_table()


def downgrade() -> None:
    op.drop_table("ingredient")
