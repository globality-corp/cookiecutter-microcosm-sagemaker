"""
Create the application.

"""
from microcosm.api import create_object_graph
from microcosm.loaders import load_each

import {{ cookiecutter.package_name }}.bundles  # noqa: 401
import {{ cookiecutter.package_name }}.evaluations  # noqa: 401
import {{ cookiecutter.package_name }}.routes  # noqa: 401
from {{ cookiecutter.package_name }}.app_hooks.serve.config import load_default_config


def create_app(debug=False,
               testing=False,
               model_only=False,
               loaders=[]):
    """
    Create the object graph for serving.

    """
    loader = load_each(
        load_default_config,
        *loaders,
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

        # bundles
        "example_bundle",
    )

    if not model_only:
        graph.use(
            # conventions
            "swagger_convention",
            "ping_convention",

            # routes
            "invocations_route",
        )

    return graph.lock()
