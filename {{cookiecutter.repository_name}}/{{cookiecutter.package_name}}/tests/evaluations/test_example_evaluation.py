from microcosm_sagemaker.testing.evaluation import EvaluationTestCase

from {{cookiecutter.package_name}}.tests.fixtures import get_fixture_path


class TestExampleEvaluation(EvaluationTestCase):
    """
    Loads the given artifact and runs the `example_evaluation` with the given
    input data.

    """

    # Indicates which evaluation we are testing.  This name will be used to
    # access the evaluation from the dependency graph.
    evaluation_name = "example_evaluation"

    # An input artifact that will be used to load a bundle to evaluate
    root_input_artifact_path = get_fixture_path("artifact")

    # Data to use to test the evaluation
    input_data_path = get_fixture_path("input_data")
