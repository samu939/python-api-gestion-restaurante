"""create_plate_table

Revision ID: f1143d118c4b
Revises: af8ed4b68d96
Create Date: 2024-07-01 22:13:18.328958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1143d118c4b'
down_revision = 'af8ed4b68d96'
branch_labels = None
depends_on = None

def create_plate_table():
    conn = op.get_bind()
    conn.execute("""
                 create table if not exists plate(
	id varchar PRIMARY KEY DEFAULT uuid_generate_v4(),
	name varchar(20) UNIQUE NOT NULL,
	description varchar(200) NOT NULL,
	price float NOT NULL,
	constraint price_greater_than_cero CHECK (price > 0)
);

                 """)

def upgrade() -> None:
    create_plate_table()


def downgrade() -> None:
    op.drop_table("plate")
