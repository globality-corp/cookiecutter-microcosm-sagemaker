"""
Create the application.

"""
from typing import Callable

from microcosm.api import create_object_graph
from microcosm.config.model import Configuration
from microcosm.loaders import load_each, load_from_environ
from microcosm.metadata import Metadata
from microcosm.object_graph import ObjectGraph
from microcosm_sagemaker.loaders import train_conventions_loader

import {{ cookiecutter.package_name }}.bundles  # noqa: 401
from {{ cookiecutter.package_name }}.app_hooks.train.config import load_default_config


Loader = Callable[[Metadata], Configuration]
empty_loader = load_each()


def create_app(
    debug: bool = False,
    testing: bool = False,
    extra_loader: Loader = empty_loader,
) -> ObjectGraph:
    """
    Create the object graph for the application.

    """

    loader = train_conventions_loader(
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
    )

    return graph.lock()
