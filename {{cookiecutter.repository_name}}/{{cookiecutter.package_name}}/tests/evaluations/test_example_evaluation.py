from microcosm_sagemaker.testing.evaluation import EvaluationTestCase

from {{ cookiecutter.package_name }}.tests.fixtures import get_fixture_path


class TestExampleEvaluation(EvaluationTestCase):
    """
    Loads the given artifact and runs the `example_evaluation` with the given
    input data.

    """
    evaluation_name = "example_evaluation"
    root_input_artifact_path = get_fixture_path("example_input_artifact")
    input_data_path = get_fixture_path("example_input_data")
