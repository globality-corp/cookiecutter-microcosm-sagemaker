"""
Create the application.

"""
from typing import Callable, Iterable, Optional

from microcosm.api import create_object_graph
from microcosm.config.model import Configuration
from microcosm.loaders import load_each
from microcosm.metadata import Metadata
from microcosm.object_graph import ObjectGraph

import {{ cookiecutter.package_name }}.bundles  # noqa: 401
import {{ cookiecutter.package_name }}.evaluations  # noqa: 401
from {{ cookiecutter.package_name }}.app_hooks.evaluate.config import load_default_config


Loader = Callable[[Metadata], Configuration]


def create_app(
    debug: bool = False,
    testing: bool = False,
    loaders: Optional[Iterable[Loader]] = None,
) -> ObjectGraph:
    """
    Create the object graph for serving.

    """
    if loaders is None:
        loaders = []

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
    )

    return graph.lock()
