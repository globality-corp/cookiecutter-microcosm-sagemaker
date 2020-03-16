"""
Create the application.

"""
from typing import Callable, Iterable, Optional

from microcosm.api import create_object_graph
from microcosm.config.model import Configuration
from microcosm.loaders import empty_loader, load_each, load_from_environ
from microcosm.loaders.compose import load_config_and_secrets
from microcosm.metadata import Metadata
from microcosm.object_graph import ObjectGraph
from microcosm_sagemaker.loaders import serve_conventions_loader
from microcosm_secretsmanager.loaders.conventions import load_from_secretsmanager

import {{ cookiecutter.package_name }}.bundles  # noqa: 401
import {{ cookiecutter.package_name }}.evaluations  # noqa: 401
import {{ cookiecutter.package_name }}.routes  # noqa: 401
from {{ cookiecutter.package_name }}.app_hooks.serve.config import load_default_config


Loader = Callable[[Metadata], Configuration]


def create_app(
    debug=False,
    testing=False,
    model_only=False,
    extra_loader=empty_loader,
) -> ObjectGraph:
    """
    Create the object graph for serving.
    """

    loader = serve_conventions_loader(
        initial_loader=load_each(
            load_default_config,
            load_from_environ,
            extra_loader,
        )
    )

    partitioned_loader = load_config_and_secrets(
        config=loader,
        secrets=load_from_secretsmanager(),
    )

    graph = create_object_graph(
        name=__name__.split(".")[0],
        debug=debug,
        testing=testing,
        loader=partitioned_loader,
    )

    graph.use(
        "logging",

        # Sagemaker basics
        "sagemaker",

        # This line causes active bundle and its dependencies to automatically
        # be loaded from the configured input artifact.
        "load_active_bundle_and_dependencies",
    )

    if not model_only:
        graph.use(
            # API Conventions
            "discovery_convention",
            "health_convention",
            "landing_convention",
            "config_convention",

            # Routes
            "invocations_route",

            "v1_swagger_convention",
        )

    return graph.lock()
