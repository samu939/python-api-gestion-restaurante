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
    conn = op.get_bind()
    conn.execute(""" create table if not exists ingredient_store(
	id varchar PRIMARY KEY DEFAULT uuid_generate_v4(),
	quantity int NOT NULL,
	fk_store varchar NOT NULL,
	fk_ingredient varchar NOT NULL,
	constraint fk_store FOREIGN KEY(fk_store) REFERENCES store(id),
	constraint fk_ingredient FOREIGN KEY(fk_ingredient) REFERENCES ingredient(id),
	constraint store_ingredient_quantity_greater_than_cero CHECK (quantity > 0)
    );
    """)

def upgrade() -> None:
    create_ingredient_store_table()


def downgrade() -> None:
    op.drop_table('ingredient_store')
