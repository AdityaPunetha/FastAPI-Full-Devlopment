"""add content column

Revision ID: 8b99830b911a
Revises: 5772843f4787
Create Date: 2023-03-22 15:37:31.829432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8b99830b911a"
down_revision = "5772843f4787"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
