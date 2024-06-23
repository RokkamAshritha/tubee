"""Action Tag Integration

Revision ID: 8271190eec99
Revises: 9474e9817305
Create Date: 2021-01-27 01:43:19.571472

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "8271190eec99"
down_revision = "9474e9817305"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("action", schema=None) as batch_op:
        batch_op.add_column(sa.Column("tag_id", sa.Integer(), nullable=True))
        batch_op.alter_column(
            "username", existing_type=sa.VARCHAR(length=32), nullable=False
        )
        batch_op.create_foreign_key(
            batch_op.f("fk_action_tag_id_tag"), "tag", ["tag_id"], ["id"]
        )
        batch_op.create_foreign_key(
            batch_op.f("fk_action_channel_id_channel"),
            "channel",
            ["channel_id"],
            ["id"],
        )

    with op.batch_alter_table("tag", schema=None) as batch_op:
        batch_op.alter_column(
            "username", existing_type=sa.VARCHAR(length=32), nullable=False
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("tag", schema=None) as batch_op:
        batch_op.alter_column(
            "username", existing_type=sa.VARCHAR(length=32), nullable=True
        )

    with op.batch_alter_table("action", schema=None) as batch_op:
        batch_op.drop_constraint(
            batch_op.f("fk_action_channel_id_channel"), type_="foreignkey"
        )
        batch_op.drop_constraint(batch_op.f("fk_action_tag_id_tag"), type_="foreignkey")
        batch_op.alter_column(
            "username", existing_type=sa.VARCHAR(length=32), nullable=True
        )
        batch_op.drop_column("tag_id")

    # ### end Alembic commands ###
