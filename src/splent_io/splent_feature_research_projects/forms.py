from flask_wtf import FlaskForm
from wtforms import SubmitField


class SplentFeatureResearchProjectsForm(FlaskForm):
    submit = SubmitField("Save splent_feature_research_projects")
