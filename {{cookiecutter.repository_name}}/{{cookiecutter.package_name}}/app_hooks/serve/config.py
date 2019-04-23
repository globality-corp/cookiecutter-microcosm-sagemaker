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
        flask=dict(
            port=8080,
        ),
        logging=dict(
            levels=dict(
                override=dict(
                    warn=[],
                ),
            ),
        ),
        swagger_convention=dict(
            version="v1",
        ),
        # We want our routes to come directly after the root /
        build_route_path=dict(
            prefix="",
        ),
    )

    return config
