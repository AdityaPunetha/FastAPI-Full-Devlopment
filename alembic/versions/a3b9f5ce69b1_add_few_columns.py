"""add few columns

Revision ID: a3b9f5ce69b1
Revises: caea595b4781
Create Date: 2023-03-22 16:05:21.228802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a3b9f5ce69b1"
down_revision = "caea595b4781"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
