from splent_framework.db import db


class ResearchProjectMixin:
    """Research-specific fields layered on top of the generic Project model.

    Applied to ``Project`` via ``refine_model``; the columns live on the shared
    ``project`` table and are created by this feature's ALTER TABLE migration.
    """

    acronym = db.Column(db.String(64), default="")
    principal_investigator = db.Column(db.String(255), default="")
    funding_agency = db.Column(db.String(255), default="")
    programme = db.Column(db.String(255), default="")
    reference = db.Column(db.String(128), default="")
    budget = db.Column(db.String(64), default="")
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    partners = db.Column(db.Text, default="")
    role = db.Column(db.String(64), default="")  # coordinator | partner
