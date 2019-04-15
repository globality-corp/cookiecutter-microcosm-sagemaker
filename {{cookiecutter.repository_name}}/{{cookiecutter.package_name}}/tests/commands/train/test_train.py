from pathlib import Path

from hamcrest import has_entries
from microcosm_sagemaker.testing.json_matcher import json_matches
from microcosm_sagemaker.testing.train import TrainCliTestCase

from {{ cookiecutter.package_name }}.tests.fixtures import get_fixture_path


class TestTrainCli(TrainCliTestCase):
    def test_train(self):
        configuration_matcher = json_matches(has_entries(
            example_bundle=has_entries(
                example_param=1.0,
            ),
        ))

        super().test_train(
            input_data_path=get_fixture_path('example_input_data'),
            gold_output_artifact_path=get_fixture_path('example_gold_output_artifact'),
            output_artifact_matchers={
                Path('configuration.json'): configuration_matcher,
            }
        )
