"""create_ingredient_plate_table

Revision ID: 24a766262e77
Revises: f1143d118c4b
Create Date: 2024-07-01 22:17:07.829075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24a766262e77'
down_revision = 'f1143d118c4b'
branch_labels = None
depends_on = None

def create_ingredient_plate_table():
    conn = op.get_bind()
    conn.execute("""
                 create table if not exists ingredient_plate(
	id varchar PRIMARY KEY DEFAULT uuid_generate_v4(),
	quantity float NOT NULL,
	fk_plate varchar NOT NULL,
	fk_ingredient varchar NOT NULL,
	constraint fk_plate FOREIGN KEY(fk_plate) REFERENCES plate(id),
	constraint fk_ingredient FOREIGN KEY(fk_ingredient) REFERENCES ingredient(id),
	constraint ingredients_in_plate_quantity_greater_than_cero CHECK (quantity > 0)
);

                 """)

def upgrade() -> None:
    create_ingredient_plate_table()


def downgrade() -> None:
    op.drop_table("ingredient_plate")
