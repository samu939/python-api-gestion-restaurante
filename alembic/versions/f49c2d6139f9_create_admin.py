"""create_admin

Revision ID: f49c2d6139f9
Revises: 5a21f63564b0
Create Date: 2024-07-02 13:21:50.634819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f49c2d6139f9'
down_revision = '5a21f63564b0'
branch_labels = None
depends_on = None

def create_admin():
    conn = op.get_bind()
    conn.execute(
        """
        INSERT INTO "public"."user" ("id", "name", "username", "password", "role") VALUES
('2ea9c01c-4c71-4d8c-9dd7-3e6f2e2243e0', 'admin', 'admin', '$2a$12$MIYapjwU9TQZBmpSGU6ppuJffYleEEjeVOGF7TaJb3w8STa4hmsGa', 'administrador');
        """
    )

def upgrade() -> None:
    create_admin()


def downgrade() -> None:
    op.execute('DELETE FROM "public"."user" WHERE username = "admin"')
