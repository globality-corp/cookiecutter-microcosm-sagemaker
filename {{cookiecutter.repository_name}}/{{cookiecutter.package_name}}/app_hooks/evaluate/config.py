"""
Configure the application.

"""
from microcosm.config.model import Configuration
from microcosm.metadata import Metadata


def load_default_config(metadata: Metadata) -> Configuration:
    """
    Construct application default configuration.

    There should be very little here.

    """

    config = Configuration(
        active_bundle="example_bundle",
        active_evaluation="example_evaluation",
    )

    return config
