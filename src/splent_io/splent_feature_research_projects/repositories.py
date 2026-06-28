from splent_io.splent_feature_research_projects.models import ResearchProjects
from splent_framework.repositories.BaseRepository import BaseRepository


class ResearchProjectsRepository(BaseRepository):
    def __init__(self):
        super().__init__(ResearchProjects)
