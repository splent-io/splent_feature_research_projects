"""Add research-specific fields to the shared project table.

This refinement does not own a table; it extends the base 'projects' feature's
``project`` table with research columns via manual ALTER TABLE operations.

Revision ID: rp0001_research
Revises:
"""

import sqlalchemy as sa
from alembic import op

revision = "rp0001_research"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("project", sa.Column("acronym", sa.String(length=64), nullable=True))
    op.add_column("project", sa.Column("principal_investigator", sa.String(length=255), nullable=True))
    op.add_column("project", sa.Column("funding_agency", sa.String(length=255), nullable=True))
    op.add_column("project", sa.Column("programme", sa.String(length=255), nullable=True))
    op.add_column("project", sa.Column("reference", sa.String(length=128), nullable=True))
    op.add_column("project", sa.Column("budget", sa.String(length=64), nullable=True))
    op.add_column("project", sa.Column("start_date", sa.Date(), nullable=True))
    op.add_column("project", sa.Column("end_date", sa.Date(), nullable=True))
    op.add_column("project", sa.Column("partners", sa.Text(), nullable=True))
    op.add_column("project", sa.Column("role", sa.String(length=64), nullable=True))


def downgrade():
    for name in (
        "acronym",
        "principal_investigator",
        "funding_agency",
        "programme",
        "reference",
        "budget",
        "start_date",
        "end_date",
        "partners",
        "role",
    ):
        op.drop_column("project", name)
