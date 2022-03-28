import pytest


pytest_plugins = "pytest_sagemaker"


def pytest_collection_modifyitems(config, items):
    """
    If passing a marker, do default pytest behavior
    Otherwise, skip all those with the marker requires_artifact

    This way, by default we don't run artifact tests
    """

    if config.option.markexpr != "":
        return

    skip_requires_artifact = pytest.mark.skip(reason="requires artifact")
    for item in items:
        if "requires_artifact" in item.keywords:
            item.add_marker(skip_requires_artifact)
