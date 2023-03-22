"""add foreign key

Revision ID: caea595b4781
Revises: 2cb4f1948731
Create Date: 2023-03-22 15:59:02.200752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "caea595b4781"
down_revision = "2cb4f1948731"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
