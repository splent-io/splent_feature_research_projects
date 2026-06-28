# research_projects adds no routes of its own. It reuses the public and admin
# routes from the base 'projects' feature, refines the Project model with
# research fields, and overrides the projects templates. The blueprint exists
# only so those template overrides take precedence over the base feature.
from splent_io.splent_feature_research_projects import research_projects_bp  # noqa: F401
