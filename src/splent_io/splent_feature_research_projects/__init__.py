from splent_framework.blueprints.base_blueprint import create_blueprint
from splent_framework.refinement import refine_model

from splent_io.splent_feature_research_projects.models import ResearchProjectMixin

# A blueprint is registered so this feature's template overrides
# (templates/projects/*.html) take precedence over the base projects feature.
research_projects_bp = create_blueprint(__name__)


def init_feature(app):
    from splent_framework.assets.asset_registry import register_asset

    # Layer research-specific fields onto the base Project model.
    refine_model("Project", ResearchProjectMixin)
    # Public research-project detail stylesheet (the scientific field grid).
    # Token-driven; styled by the active skin. order=110 so it layers after the
    # base projects.css.
    register_asset(
        "css",
        "research_projects.assets",
        order=110,
        subfolder="css",
        filename="research_projects.css",
    )


def inject_context_vars(app):
    return {}
