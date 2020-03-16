"""
Create the application.

"""
from typing import Iterable, Optional

from microcosm.api import create_object_graph
from microcosm.loaders import empty_loader, load_each, load_from_environ
from microcosm.object_graph import ObjectGraph
from microcosm_sagemaker.loaders import train_conventions_loader

import {{ cookiecutter.package_name }}.bundles  # noqa: 401
import {{ cookiecutter.package_name }}.evaluations  # noqa: 401
from {{cookiecutter.package_name}}.app_hooks.train.config import (
    load_default_config,
)


def create_app(
    debug=False,
    testing=False,
    extra_config=None,
    extra_loader=empty_loader
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

        # Bundles
        "example_bundle",
    )

    return graph.lock()
