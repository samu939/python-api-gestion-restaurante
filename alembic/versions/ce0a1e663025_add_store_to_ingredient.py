"""add store to ingredient

Revision ID: ce0a1e663025
Revises: 95af1febcd51
Create Date: 2024-06-13 09:01:16.928920

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = 'ce0a1e663025'
down_revision = '95af1febcd51'
branch_labels = None
depends_on = None

def alter_ingredients_table():
    op.add_column("ingredients", 
                  sa.Column("store_id", UUID, sa.ForeignKey("store.id"), nullable=True))


def upgrade() -> None:
    alter_ingredients_table()


def downgrade() -> None:
    pass