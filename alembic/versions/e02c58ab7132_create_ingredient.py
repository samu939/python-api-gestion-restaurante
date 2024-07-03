"""create_ingredient

Revision ID: e02c58ab7132
Revises: f49c2d6139f9
Create Date: 2024-07-02 17:58:06.736228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e02c58ab7132'
down_revision = 'f49c2d6139f9'
branch_labels = None
depends_on = None

def create_ingredient():
    conn = op.get_bind()
    conn.execute(
        """
        INSERT INTO "public"."ingredient" ("id", "name") VALUES
        ('3fa85f64-5717-4562-b3fc-2c963f66afa6', 'ingredient 1');
        
        INSERT INTO "public"."store" (id, name) VALUES('3fa85f64-5717-4562-b3fc-2c963f66afa6', 'store 1');

        INSERT INTO "public"."ingredient_store" (id, fk_ingredient, fk_store, quantity) VALUES('3fa85f64-5717-4562-b3fc-2c963f66afa6', '3fa85f64-5717-4562-b3fc-2c963f66afa6', '3fa85f64-5717-4562-b3fc-2c963f66afa6', 10)
        
        """
    )

def upgrade() -> None:
    create_ingredient()


def downgrade() -> None:
    op.execute("""
                DELETE FROM "public"."ingredient_store" WHERE fk_ingredient = '3fa85f64-5717-4562-b3fc-2c963f66afa6';
                DELETE FROM "public"."store" WHERE name = 'store 1';
                DELETE FROM "public"."ingredient_plate" WHERE fk_ingredient = '3fa85f64-5717-4562-b3fc-2c963f66afa6';
                DELETE FROM "public"."ingredient" WHERE name = 'ingredient 1';
               """)
