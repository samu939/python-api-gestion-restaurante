"""create_store_table

Revision ID: 71f65961713f
Revises: 36cc34b5b1f2
Create Date: 2024-07-01 20:50:11.132960

"""
from uuid import uuid4
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

from db.db_base import table_exists

# revision identifiers, used by Alembic.
revision = '71f65961713f'
down_revision = '36cc34b5b1f2'
branch_labels = None
depends_on = None

def create__store_table():
    if not table_exists("store"):
        op.create_table("store", 
                    sa.Column("id", sa.String(),  primary_key=True, default=uuid4()),
                    sa.Column("name", sa.String(40), index=True, nullable=False))


def upgrade() -> None:
    create__store_table()


def downgrade() -> None:
    op.drop_table("store")
