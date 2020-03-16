from pathlib import Path

from hamcrest import has_entries
from microcosm_sagemaker.testing.bytes_extractor import (
    ExtractorMatcherPair,
    json_extractor,
)
from microcosm_sagemaker.testing.train import TrainCliTestCase

from {{cookiecutter.package_name}}.tests.fixtures import get_fixture_path


class TestTrainCli(TrainCliTestCase):
    input_data_path = get_fixture_path("example_input_data")

    @property
    def output_artifact_matchers(self):
        configuration_extractor_matcher = ExtractorMatcherPair(
            extractor=json_extractor,
            matcher_constructor=has_entries(
                example_bundle=has_entries(
                    example_param=1.0,
                ),
            ),
        )

        return {
            Path("configuration.json"): configuration_extractor_matcher,
        }
