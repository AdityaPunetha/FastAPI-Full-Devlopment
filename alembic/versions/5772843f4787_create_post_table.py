"""Create post table

Revision ID: 5772843f4787
Revises: 
Create Date: 2023-03-22 15:30:53.477503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5772843f4787"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
