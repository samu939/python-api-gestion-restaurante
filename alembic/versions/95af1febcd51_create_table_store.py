"""create table store

Revision ID: 95af1febcd51
Revises: 43d70d079518
Create Date: 2024-06-13 08:56:27.039509

"""
from uuid import uuid4
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '95af1febcd51'
down_revision = '43d70d079518'
branch_labels = None
depends_on = None

def create_store_table():
    op.create_table(
        "store",
        sa.Column("id", UUID, primary_key=True, default=uuid4()),
        sa.Column("name", sa.Text, nullable=False)
    )


def upgrade() -> None:
    create_store_table()


def downgrade() -> None:
    op.drop_table("store")
