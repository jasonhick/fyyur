"""empty message

Revision ID: fc50206723be
Revises: 
Create Date: 2024-10-08 18:40:24.540071

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "fc50206723be"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "artists",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("city", sa.String(length=120), nullable=True),
        sa.Column("county", sa.String(length=120), nullable=True),
        sa.Column("facebook_link", sa.String(length=120), nullable=True),
        sa.Column("genres", sa.ARRAY(sa.String()), nullable=True),
        sa.Column("image_link", sa.String(length=500), nullable=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("phone", sa.String(length=120), nullable=True),
        sa.Column("seeking_description", sa.String(length=500), nullable=True),
        sa.Column("seeking_talent", sa.Boolean(), nullable=True),
        sa.Column("seeking_venue", sa.Boolean(), nullable=True),
        sa.Column("website_link", sa.String(length=500), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "venues",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("address", sa.String(length=120), nullable=False),
        sa.Column("city", sa.String(length=120), nullable=False),
        sa.Column("county", sa.String(length=120), nullable=True),
        sa.Column("facebook_link", sa.String(length=120), nullable=True),
        sa.Column("genres", sa.ARRAY(sa.String()), nullable=True),
        sa.Column("image_link", sa.String(length=500), nullable=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("phone", sa.String(length=120), nullable=False),
        sa.Column("seeking_description", sa.String(length=500), nullable=True),
        sa.Column("seeking_talent", sa.Boolean(), nullable=True),
        sa.Column("website_link", sa.String(length=500), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "shows",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("start_time", sa.DateTime(), nullable=True),
        sa.Column("artist_id", sa.Integer(), nullable=False),
        sa.Column("venue_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["artist_id"],
            ["artists.id"],
        ),
        sa.ForeignKeyConstraint(
            ["venue_id"],
            ["venues.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("shows")
    op.drop_table("venues")
    op.drop_table("artists")
    # ### end Alembic commands ###
