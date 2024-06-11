"""create ingredients table

Revision ID: 88ec9bb40650
Revises: 492eec39b72d
Create Date: 2024-06-11 14:41:11.373726

"""
from uuid import uuid4
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '88ec9bb40650'
down_revision = '492eec39b72d'
branch_labels = None
depends_on = None


def create_ingredients_table():
    op.create_table(
        "ingredients",
        sa.Column("id", UUID, primary_key=True, default=uuid4()),
        sa.Column("name", sa.Text, nullable=False),
    )


def upgrade() -> None:
    create_ingredients_table()


def downgrade() -> None:
    op.drop_table("ingredients")
