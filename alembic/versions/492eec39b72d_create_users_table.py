"""create users table

Revision ID: 492eec39b72d
Revises: 8e0c5b7e9066
Create Date: 2022-10-11 18:39:19.297356

"""
from uuid import uuid4

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = "492eec39b72d"
down_revision = "4d495ae5b0ff"
branch_labels = None
depends_on = None


def create_users_table():
    op.create_table(
        "users",
        sa.Column("id", UUID, primary_key=True, default=uuid4()),
        sa.Column("username", sa.String(40), unique=True, index=True, nullable=False),
        sa.Column("name", sa.Text, nullable=False),
        sa.Column("password", sa.Text, nullable=False),
        sa.Column("role", sa.Text, nullable=False),
    )


def upgrade() -> None:
    create_users_table()


def downgrade() -> None:
    op.drop_table("users")
