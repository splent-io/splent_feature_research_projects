from splent_framework.blueprints.base_blueprint import create_blueprint
from splent_framework.refinement import refine_model

from splent_io.splent_feature_research_projects.models import ResearchProjectMixin

# A blueprint is registered so this feature's template overrides
# (templates/projects/*.html) take precedence over the base projects feature.
research_projects_bp = create_blueprint(__name__)


def init_feature(app):
    # Layer research-specific fields onto the base Project model.
    refine_model("Project", ResearchProjectMixin)


def inject_context_vars(app):
    return {}
