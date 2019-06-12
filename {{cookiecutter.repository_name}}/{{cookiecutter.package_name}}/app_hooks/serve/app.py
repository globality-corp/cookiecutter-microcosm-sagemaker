"""
Create the application.

"""
from microcosm.api import create_object_graph
from microcosm.loaders import empty_loader, load_each, load_from_environ
from microcosm.object_graph import ObjectGraph
from microcosm.typing import Loader
from microcosm_sagemaker.loaders import serve_conventions_loader

import {{ cookiecutter.package_name }}.bundles  # noqa: 401
import {{ cookiecutter.package_name }}.evaluations  # noqa: 401
import {{ cookiecutter.package_name }}.routes  # noqa: 401
from {{ cookiecutter.package_name }}.app_hooks.serve.config import load_default_config


def create_app(
    debug: bool = False,
    testing: bool = False,
    model_only: bool = False,
    extra_loader: Loader = empty_loader,
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

    graph = create_object_graph(
        name=__name__.split(".")[0],
        debug=debug,
        testing=testing,
        loader=loader,
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
            # SageMaker conventions
            "ping_convention",

            # Routes
            "invocations_route",
        )

    return graph.lock()
