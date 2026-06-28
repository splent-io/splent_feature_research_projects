"""
CLI commands contributed by splent_feature_research_projects.

These commands are auto-discovered by the framework and exposed in the
SPLENT CLI under the ``feature:research_projects`` group.

Usage::

    splent feature:research_projects hello
"""

import click


@click.command("hello")
def hello():
    """Example command — replace with your own."""
    click.echo("  Hello from splent_feature_research_projects!")


cli_commands = [hello]
