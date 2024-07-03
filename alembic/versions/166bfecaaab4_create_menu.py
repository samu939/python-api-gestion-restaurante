"""create_menu

Revision ID: 166bfecaaab4
Revises: f1e14dc7cbc2
Create Date: 2024-07-02 21:19:58.434306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '166bfecaaab4'
down_revision = 'f1e14dc7cbc2'
branch_labels = None
depends_on = None

def create_menu():
    conn = op.get_bind()
    conn.execute(
        """
        INSERT INTO "public"."menu" ("id", "name") VALUES
        ('1ccc98db-af71-4127-bbc2-d4e0e4449961', 'Menu 1');
        
        INSERT INTO "public"."menu_plate" ("id", "fk_menu", "fk_plate") VALUES
        ('3fa85f64-5717-4562-b3fc-2c963f66afa6', '1ccc98db-af71-4127-bbc2-d4e0e4449961', 'a40f5bc4-398f-446c-a11b-b6d45815840e');
        
        """
    )
    


def upgrade() -> None:
    create_menu()


def downgrade() -> None:
    
    
    op.execute("""
                DELETE FROM "public"."menu_plate" 
                DELETE FROM "public"."menu"
                DELETE FROM "public"."plate"
               """)
