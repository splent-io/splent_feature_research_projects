"""
Functional tests for splent_feature_research_projects.

Functional tests use Flask's test client to exercise full HTTP
request/response cycles (GET, POST, redirects, rendered HTML).

This feature is a refinement: it registers no routes of its own, it
extends the projects feature with academic metadata and overrides its
templates. The scaffolded test asked for /research_projects, which never
existed. What matters instead is that the refined feature still serves
its pages once this one is installed on top.
"""


def test_refined_projects_index_still_serves(test_client):
    response = test_client.get("/projects")
    assert response.status_code in (200, 302)


def test_refined_projects_admin_is_registered(test_client):
    response = test_client.get("/admin/projects")
    assert response.status_code in (200, 302)
