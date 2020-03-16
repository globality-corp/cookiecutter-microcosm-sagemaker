"""
Create the application.

"""
from typing import Callable, Iterable, Optional

from microcosm.api import create_object_graph
from microcosm.config.model import Configuration
from microcosm.loaders import empty_loader, load_each, load_from_environ
from microcosm.metadata import Metadata
from microcosm.object_graph import ObjectGraph
from microcosm_sagemaker.loaders import evaluate_conventions_loader

import {{ cookiecutter.package_name }}.bundles  # noqa: 401
import {{ cookiecutter.package_name }}.evaluations  # noqa: 401
from {{ cookiecutter.package_name }}.app_hooks.evaluate.config import load_default_config


Loader = Callable[[Metadata], Configuration]


def create_app(
    debug=False,
    testing=False,
    model_only=False,
    extra_loader=empty_loader,
) -> ObjectGraph:
    """
    Create the object graph for evaluation.
    """

    loader = evaluate_conventions_loader(
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

        # Bundles
        "example_bundle",

        # Evaluations
        "example_evaluation",
    )

    return graph.lock()
