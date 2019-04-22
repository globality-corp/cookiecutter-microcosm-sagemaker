"""
Create the application.

"""
from microcosm.api import create_object_graph
from microcosm.loaders import load_each, load_from_dict, load_from_environ
from microcosm_sagemaker.loaders import load_train_conventions

import {{ cookiecutter.package_name }}.bundles  # noqa: 401
from {{ cookiecutter.package_name }}.app_hooks.train.config import load_default_config


def create_app(debug=False, testing=False, extra_config={}, extra_deps=[]):
    """
    Create the object graph for the application.

    """
    config_loader = load_each(
        load_default_config,
        load_from_dict(extra_config),
        load_from_environ,
        load_train_conventions,
    )

    graph = create_object_graph(
        name=__name__.split(".")[0],
        debug=debug,
        testing=testing,
        loader=config_loader,
    )

    graph.use(
        "logging",

        # Sagemaker basics
        "sagemaker",

        # Bundles
        "example_bundle",
    )
    graph.use(*extra_deps)

    return graph.lock()
