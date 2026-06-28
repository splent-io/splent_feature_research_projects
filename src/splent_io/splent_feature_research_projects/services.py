from splent_io.splent_feature_research_projects.repositories import ResearchProjectsRepository
from splent_framework.services.BaseService import BaseService


class ResearchProjectsService(BaseService):
    def __init__(self):
        super().__init__(ResearchProjectsRepository())
