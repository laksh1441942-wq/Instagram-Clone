"""create application tables

Revision ID: 6bb83d43e2c7
Revises:
Create Date: 2026-11-05 21:22:41.222519

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "6bb83d43e2c7"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create the schema required by the current application models."""
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    existing_tables = set(inspector.get_table_names())

    if "User_Table" not in existing_tables:
        op.create_table(
            "User_Table",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("username", sa.String(), nullable=True),
            sa.Column("email", sa.String(), nullable=False, unique=True),
            sa.Column("hashed_password", sa.String(), nullable=False),
            sa.Column("is_active", sa.Boolean(), nullable=False, default=True),
            sa.Column("created_at", sa.DateTime(), nullable=False),
            sa.Column("name", sa.String(), nullable=False),
            sa.Column("dob", sa.DateTime(), nullable=False),
            sa.Column("gender", sa.String(), nullable=False),
            sa.Column("profile_pic", sa.String(), nullable=False),
            sa.Column("bio", sa.String(), nullable=False),
            sa.Column("location", sa.String(), nullable=False),
        )

    if "Post_Table" not in existing_tables:
        op.create_table(
            "Post_Table",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column(
                "author_id",
                sa.Integer(),
                sa.ForeignKey("User_Table.id"),
                nullable=False,
            ),
            sa.Column("title", sa.String(), nullable=False),
            sa.Column("content", sa.String(), nullable=False),
            sa.Column("image", sa.String(), nullable=False),
            sa.Column("created_at", sa.DateTime(), nullable=False),
            sa.Column("location", sa.String(), nullable=False),
            sa.Column("likes_count", sa.Integer(), nullable=False, default=0),
        )

    if "Like_Posts" not in existing_tables:
        op.create_table(
            "Like_Posts",
            sa.Column("like_id", sa.Integer(), primary_key=True),
            sa.Column("post_id", sa.Integer(), sa.ForeignKey("Post_Table.id")),
            sa.Column("user_id", sa.Integer(), sa.ForeignKey("User_Table.id")),
        )

    if "Hash_Tag_Model" not in existing_tables:
        op.create_table(
            "Hash_Tag_Model",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("name", sa.String(), nullable=False),
        )
        op.create_index("ix_Hash_Tag_Model_name", "Hash_Tag_Model", ["name"])

    if "Hash_Tag_Table" not in existing_tables:
        op.create_table(
            "Hash_Tag_Table",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("post_id", sa.Integer(), sa.ForeignKey("Post_Table.id")),
            sa.Column("hashtag_id", sa.Integer(), sa.ForeignKey("Hash_Tag_Model.id")),
        )

    if "Reset_Password" not in existing_tables:
        op.create_table(
            "Reset_Password",
            sa.Column("email", sa.String(), primary_key=True, unique=True),
            sa.Column("code", sa.String(), nullable=False),
        )


def downgrade() -> None:
    """Drop the application schema."""
    op.drop_table("Reset_Password")
    op.drop_table("Hash_Tag_Table")
    op.drop_index("ix_Hash_Tag_Model_name", table_name="Hash_Tag_Model")
    op.drop_table("Hash_Tag_Model")
    op.drop_table("Like_Posts")
    op.drop_table("Post_Table")
    op.drop_table("User_Table")
