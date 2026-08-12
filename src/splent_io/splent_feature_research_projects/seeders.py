import os
import re

from splent_framework.db import db
from splent_framework.seeders.BaseSeeder import BaseSeeder

from splent_io.splent_feature_projects.models import Project

# Media is an optional soft dependency: when the feature is present the seeder
# registers each project logo and stores its public URL on Project.image.
try:
    from splent_io.splent_feature_media.services import MediaService
except ImportError:
    MediaService = None


def _slugify(value: str) -> str:
    value = value.lower().strip()
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def _status(raw: str) -> str:
    return "active" if raw.strip().lower() == "active" else "past"


# Real research projects of the lab. Research fields (programme / funding
# agency / dates) come from the migrated site export where available; the
# rest can be completed in the admin. Acronyms drive the slug.
_PROJECTS = [
    {
        "acronym": "SENSOLIVE",
        "title": "Deficit irrigation system in olive groves using dendrometers and intelligent digital twins",
        "programme": "Otros Proyectos Junta de Andalucía",
        "funding_agency": "Junta de Andalucía — Consejería de Universidad, Investigación e Innovación",
        "start": "2024-12-19",
        "end": "2026-12-18",
        "image": "sensolive.png",
        "status": "active",
    },
    {
        "acronym": "ENFOCA",
        "title": "Ensamblado de Nodos mediante Federación Optimizada de Conocimiento Autocodificado en Patología Digital",
        "programme": "Plan Estatal 2021-2023 — Proyectos de Investigación Orientada",
        "funding_agency": "Ministerio de Ciencia, Innovación y Universidades",
        "start": "2024-09-01",
        "end": "2027-12-31",
        "image": "enfoca.jpg",
        "status": "active",
    },
    {
        "acronym": "DATA-PL",
        "title": "Data-Intensive Software Product Lines",
        "programme": "Proyectos de Generación de Conocimiento 2022",
        "funding_agency": "Ministerio de Ciencia e Innovación",
        "start": "2023-09-01",
        "end": "2026-08-31",
        "image": "data-pl.png",
        "status": "active",
    },
    {
        "acronym": "METAMORFOSIS",
        "title": "Digital Transformation Framework through Customised Software on Data Management, Business Processes and Security Governance",
        "programme": "Andalusia ERDF R+D+i Projects",
        "funding_agency": "Consejería de Economía, Conocimiento, Empresas y Universidad",
        "start": "2022-01-01",
        "end": "2023-05-31",
        "image": "metamorfosis.jpg",
        "status": "past",
    },
    {
        "acronym": "COPERNICA",
        "title": "Business Process Collaboration for Good Governance of Shared Services and Data",
        "programme": "PAIDI 2020 — R&D&I Projects",
        "funding_agency": "Consejería de Economía, Conocimiento, Empresas y Universidad",
        "start": "2021-10-05",
        "end": "2022-12-31",
        "image": "copernica.png",
        "status": "past",
    },
    {
        "acronym": "TASOVA PLUS",
        "title": "Red en nuevas Tendencias en Arquitectura Software y Variabilidad",
        "programme": "Convocatoria 2022 — Redes de Investigación",
        "funding_agency": "Ministerio de Ciencia e Innovación",
        "start": "2023-06-01",
        "end": "2025-05-31",
        "image": "tasova-plus.png",
        "status": "past",
    },
    {
        "acronym": "MIDAS",
        "title": "Monitorización Inteligente y Digitalización Avanzada de Servicios de Marketing",
        "programme": "Contrato 68/83",
        "funding_agency": "Consultoría Informática Acofi",
        "start": "2023-01-01",
        "end": "2024-09-30",
        "image": "midas.png",
        "status": "past",
    },
    {
        "acronym": "AQUAIA",
        "title": "Sistema de programación de riego deficitario para cultivos (Grupo Operativo)",
        "programme": "Otros Proyectos Junta de Andalucía",
        "funding_agency": "Junta de Andalucía",
        "start": "2023-04-01",
        "end": "2025-06-30",
        "image": "aquaia.png",
        "status": "past",
    },
    {
        "acronym": "PLANT",
        "title": "Por resolver (to be resolved)",
        "programme": "",
        "funding_agency": "",
        "image": "plant.png",
        "status": "past",
    },
]


def _seed_image(filename, title=""):
    if MediaService is None:
        return ""
    path = os.path.join(os.path.dirname(__file__), "seed_media", filename)
    item = MediaService().import_from_file(
        path, title=title, source_key="seed://research_projects/" + filename
    )
    return item.url


class ResearchProjectsSeeder(BaseSeeder):
    def run(self):
        from datetime import date

        # This refinement owns the real project data: clear the generic demo
        # rows from the base 'projects' feature, then insert the real ones.
        Project.query.delete()
        db.session.commit()

        def _d(value):
            return date.fromisoformat(value) if value else None

        data = []
        for order, p in enumerate(_PROJECTS, start=1):
            data.append(
                Project(
                    title=p["title"],
                    slug=_slugify(p["acronym"] or p["title"]),
                    summary=p["title"],
                    description=p["title"],
                    status=_status(p["status"]),
                    acronym=p["acronym"],
                    programme=p.get("programme", ""),
                    funding_agency=p.get("funding_agency", ""),
                    start_date=_d(p.get("start")),
                    end_date=_d(p.get("end")),
                    image=_seed_image(p["image"], title=p["acronym"]) if p.get("image") else "",
                    order=order,
                    published=True,
                )
            )
        self.seed(data)
