"""
Configure the application.

"""
from microcosm.config.model import Configuration


def load_default_config(metadata):
    """
    Construct application default configuration.

    There should be very little here.

    """

    config = Configuration(
        active_bundle="example_bundle",
        active_evaluation="example_evaluation",
    )

    return config
