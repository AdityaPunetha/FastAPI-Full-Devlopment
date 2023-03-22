"""add user table

Revision ID: 2cb4f1948731
Revises: 8b99830b911a
Create Date: 2023-03-22 15:40:51.876456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2cb4f1948731"
down_revision = "8b99830b911a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
