"""alter table ingredient quantity int-float

Revision ID: 43d70d079518
Revises: 88ec9bb40650
Create Date: 2024-06-13 07:47:50.038446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43d70d079518'
down_revision = '88ec9bb40650'
branch_labels = None
depends_on = None

def alter_ingredients_table():
    op.alter_column(
        table_name= "ingredients",
        column_name= "quantity",
        type_= sa.Float
    )


def upgrade() -> None:
    alter_ingredients_table()


def downgrade() -> None:
    pass