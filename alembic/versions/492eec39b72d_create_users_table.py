"""create users table

Revision ID: 492eec39b72d
Revises: 8e0c5b7e9066
Create Date: 2022-10-11 18:39:19.297356

"""
from uuid import uuid4

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

from db.db_base import table_exists


# revision identifiers, used by Alembic.
revision = "492eec39b72d"
down_revision = "4d495ae5b0ff"
branch_labels = None
depends_on = None

def create_uuid_generate_v4():
    conn = op.get_bind()
    conn.execute("""
                 CREATE OR REPLACE FUNCTION public.uuid_generate_v4()
                RETURNS uuid
                LANGUAGE c
                PARALLEL SAFE STRICT
                AS '$libdir/uuid-ossp', $function$uuid_generate_v4$function$

                 """)

def create_users_table():
    if not table_exists("user"):
        op.create_table(
            "user",
            sa.Column("id", sa.String(), primary_key=True, default=uuid4()),
            sa.Column("username", sa.String(40), unique=True, index=True, nullable=False),
            sa.Column("name", sa.Text, nullable=False),
            sa.Column("password", sa.Text, nullable=False),
            sa.Column("role", sa.Text, nullable=False),
        )


def upgrade() -> None:
    create_users_table()
    create_uuid_generate_v4()


def downgrade() -> None:
    op.drop_table("user")
    conn = op.get_bind()
    conn.execute("DROP FUNCTION public.uuid_generate_v4()")
