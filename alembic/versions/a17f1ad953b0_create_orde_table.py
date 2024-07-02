"""create_orde_table

Revision ID: a17f1ad953b0
Revises: 866704c686cc
Create Date: 2024-07-01 22:21:52.159251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a17f1ad953b0'
down_revision = '866704c686cc'
branch_labels = None
depends_on = None

def create_order_table():
    conn = op.get_bind()
    conn.execute("""
                 create table if not exists "order"(
	id varchar PRIMARY KEY DEFAULT uuid_generate_v4(),
	order_date date NOT NULL DEFAULT CURRENT_DATE,
	final_price float NOT NULL,
	fk_user varchar NOT NULL,
	constraint final_price_greater_than_cero CHECK (final_price > 0),
	constraint fk_user FOREIGN KEY(fk_user) REFERENCES "user"(id)
);

                 """)

def upgrade() -> None:
    create_order_table()


def downgrade() -> None:
    op.drop_table("order")
