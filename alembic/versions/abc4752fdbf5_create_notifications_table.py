"""create_notifications_table

Revision ID: abc4752fdbf5
Revises: 166bfecaaab4
Create Date: 2024-07-02 23:53:46.023057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abc4752fdbf5'
down_revision = '166bfecaaab4'
branch_labels = None
depends_on = None

def create_notifications_table():
    conn = op.get_bind()
    conn.execute("""
CREATE TABLE if not exists "public"."notifications" (
    "id" varchar NOT NULL DEFAULT 'uuid_generate_v4()'::character varying,
    "message" varchar NOT NULL,
    "date" date NOT NULL DEFAULT CURRENT_DATE,
    "target_user" varchar NOT NULL,
    CONSTRAINT "notifications_target_user_fkey" FOREIGN KEY ("target_user") REFERENCES "public"."user"("id")
);
                 """)

def upgrade() -> None:
    create_notifications_table()


def downgrade() -> None:
    op.drop_table("notifications")
