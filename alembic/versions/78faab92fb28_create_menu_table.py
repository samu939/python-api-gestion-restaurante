"""create_menu_table

Revision ID: 78faab92fb28
Revises: 24a766262e77
Create Date: 2024-07-01 22:18:25.743789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78faab92fb28'
down_revision = '24a766262e77'
branch_labels = None
depends_on = None

def create_menu_table():
    conn = op.get_bind()
    conn.execute("""
                 create table if not exists menu(
	id varchar PRIMARY KEY DEFAULT uuid_generate_v4(),
	name varchar(20) UNIQUE NOT NULL
);

                 """)

def upgrade() -> None:
    create_menu_table()


def downgrade() -> None:
    op.drop_table("menu")
