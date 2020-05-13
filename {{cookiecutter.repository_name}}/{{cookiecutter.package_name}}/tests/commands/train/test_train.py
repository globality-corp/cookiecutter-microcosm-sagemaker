from pathlib import Path

from hamcrest import has_entries
from hamcrest.core.base_matcher import BaseMatcher
from microcosm_sagemaker.testing.bytes_extractor import ExtractorMatcherPair, json_extractor
from microcosm_sagemaker.testing.train import TrainCliTestCase

from {{cookiecutter.package_name}}.tests.fixtures import get_fixture_path


def construct_configuration_matcher(gold_configuration) -> BaseMatcher:
    return has_entries(**gold_configuration)


class TestTrainCli(TrainCliTestCase):
    """
    Tests the train cli.  This is an end-to-end test, so doesn't need to try to
    explore all edge cases.  For more specific tests, it's better to write
    bundle tests.

    """
    # Path to a small test input dataset
    input_data_path = get_fixture_path("input_data")

    # A gold directory that will be compared to the actual artifact output from
    # running the train command
    gold_output_artifact_path = get_fixture_path("artifact")

    # Define matchers that will be used to override how the gold directory
    # comparison will be handled.  In this case, we indicate that the top-level
    # `configuration.json` file doesn't need to match exactly, but just to make
    # sure that the entries that appear in our gold `configuration.json` are as
    # expected within the actual `configuration.json`.  Other entries in the
    # actual `configuration.json` output will be ignored
    output_artifact_matchers = {
        Path("configuration.json"): ExtractorMatcherPair(
            extractor=json_extractor,
            matcher_constructor=construct_configuration_matcher,
        ),
    }
