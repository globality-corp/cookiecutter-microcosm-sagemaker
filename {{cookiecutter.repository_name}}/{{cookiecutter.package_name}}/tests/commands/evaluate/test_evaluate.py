from microcosm_sagemaker.testing.evaluate import EvaluateCliTestCase

from {{cookiecutter.package_name}}.tests.fixtures import get_fixture_path


class TestEvaluateCli(EvaluateCliTestCase):
    def test_evaluate(self) -> None:
        super().test_evaluate(
            input_data_path=get_fixture_path("example_input_data"),
            input_artifact_path=get_fixture_path("example_input_artifact"),
        )