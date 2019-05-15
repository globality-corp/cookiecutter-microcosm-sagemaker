from pathlib import Path

from hamcrest import has_entries
from hamcrest.core.base_matcher import BaseMatcher
from microcosm_sagemaker.testing.bytes_extractor import (
    ExtractorMatcherPair,
    json_extractor,
)
from microcosm_sagemaker.testing.train import TrainCliTestCase

from {{cookiecutter.package_name}}.tests.fixtures import get_fixture_path


def construct_configuration_matcher(gold_configuration) -> BaseMatcher:
    return has_entries(**gold_configuration)


class TestTrainCli(TrainCliTestCase):
    def test_train(self) -> None:
        configuration_extractor_matcher = ExtractorMatcherPair(
            extractor=json_extractor,
            matcher_constructor=construct_configuration_matcher,
        )

        self.run_and_check_train(
            input_data_path=get_fixture_path("example_input_data"),
            gold_output_artifact_path=get_fixture_path("example_gold_output_artifact"),
            output_artifact_matchers={
                Path("configuration.json"): configuration_extractor_matcher,
            }
        )
