"""add user follower counts

Revision ID: 1a2b3c4d5e6f
Revises: 6bb83d43e2c7
Create Date: 2026-11-22 00:16:19.034000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1a2b3c4d5e6f"
down_revision: Union[str, Sequence[str], None] = "6bb83d43e2c7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Add follower and following counters to User_Table."""
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    columns = {column["name"] for column in inspector.get_columns("User_Table")}

    if "follower_count" not in columns:
        op.add_column(
            "User_Table",
            sa.Column("follower_count", sa.Integer(), nullable=False, server_default="0"),
        )
    if "following_count" not in columns:
        op.add_column(
            "User_Table",
            sa.Column("following_count", sa.Integer(), nullable=False, server_default="0"),
        )


def downgrade() -> None:
    """Remove follower and following counters from User_Table."""
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    columns = {column["name"] for column in inspector.get_columns("User_Table")}

    if "following_count" in columns:
        op.drop_column("User_Table", "following_count")
    if "follower_count" in columns:
        op.drop_column("User_Table", "follower_count")
