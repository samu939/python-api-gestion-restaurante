"""create_plate

Revision ID: f1e14dc7cbc2
Revises: e02c58ab7132
Create Date: 2024-07-02 20:36:04.759185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1e14dc7cbc2'
down_revision = 'e02c58ab7132'
branch_labels = None
depends_on = None

def create_plate():
    conn = op.get_bind()
    conn.execute(
        """
        INSERT INTO "public"."plate" ("id", "name", "description", "price") VALUES
        ('a40f5bc4-398f-446c-a11b-b6d45815840e', 'Plate 1', 'Description 1', 10.0);
        
        INSERT INTO "public"."ingredient_plate" ("id", "fk_ingredient", "fk_plate", "quantity") VALUES
        ('3fa85f64-5717-4562-b3fc-2c963f66afa6', '3fa85f64-5717-4562-b3fc-2c963f66afa6', 'a40f5bc4-398f-446c-a11b-b6d45815840e', 1);
        
        """
    )

def upgrade() -> None:
    create_plate()


def downgrade() -> None:
    
    op.execute("""
                DELETE FROM "public"."ingredient_plate" WHERE fk_plate = 'a40f5bc4-398f-446c-a11b-b6d45815840e';
                DELETE FROM "public"."plate" WHERE name = 'Plate 1';
               """)
