"""create_order_detail_table

Revision ID: 5a21f63564b0
Revises: a17f1ad953b0
Create Date: 2024-07-01 22:22:34.216373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a21f63564b0'
down_revision = 'a17f1ad953b0'
branch_labels = None
depends_on = None

def create_order_detail_table():
    conn = op.get_bind()
    conn.execute("""
                 create table if not exists order_detail(
	id varchar PRIMARY KEY DEFAULT uuid_generate_v4(),
	quantity int NOT NULL,
	fk_plate varchar NOT NULL,
	fk_order varchar NOT NULL,
	constraint fk_plate FOREIGN KEY(fk_plate) REFERENCES plate(id),
	constraint fk_order FOREIGN KEY(fk_order) REFERENCES "order"(id),
	constraint plates_quantity_greater_than_cero CHECK (quantity > 0)
)

                 """)

def upgrade() -> None:
    create_order_detail_table()


def downgrade() -> None:
    op.drop_table("order_detail")
