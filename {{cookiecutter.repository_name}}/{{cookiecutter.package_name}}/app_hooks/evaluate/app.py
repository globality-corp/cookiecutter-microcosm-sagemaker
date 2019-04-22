"""
Create the application.

"""
from microcosm.api import create_object_graph
from microcosm.loaders import load_each, load_from_dict

import {{ cookiecutter.package_name }}.bundles  # noqa: 401
import {{ cookiecutter.package_name }}.evaluations  # noqa: 401


def create_app(debug=False,
               testing=False,
               extra_config={},
               input_artifact=None):
    """
    Create the object graph for serving.

    """
    loader = load_each(
        input_artifact.load_config,
        load_from_dict(extra_config),
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
        "sagemaker_metrics",
        "active_bundle",
        "active_evaluation",

        # Bundles
        "example_bundle",

        # Evaluations
        "example_evaluation",
    )

    return graph.lock()
