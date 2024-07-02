"""create_menu_plate_table

Revision ID: 866704c686cc
Revises: 78faab92fb28
Create Date: 2024-07-01 22:19:28.273979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '866704c686cc'
down_revision = '78faab92fb28'
branch_labels = None
depends_on = None

def create_menu_plate_table():
    conn = op.get_bind()
    conn.execute("""
                 create table if not exists menu_plate(
	id varchar PRIMARY KEY DEFAULT uuid_generate_v4(),
	fk_plate varchar NOT NULL,
	fk_menu varchar NOT NULL,
	constraint fk_plate FOREIGN KEY(fk_plate) REFERENCES plate(id),
	constraint fk_menu FOREIGN KEY(fk_menu) REFERENCES menu(id)
);

                 """)


def upgrade() -> None:
    create_menu_plate_table()


def downgrade() -> None:
    op.drop_table("menu_plate")
