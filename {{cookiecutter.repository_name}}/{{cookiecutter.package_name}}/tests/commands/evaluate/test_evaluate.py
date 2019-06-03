from microcosm_sagemaker.testing.evaluate import EvaluateCliTestCase

from {{cookiecutter.package_name}}.tests.fixtures import get_fixture_path


class TestEvaluateCli(EvaluateCliTestCase):
    """
    Tests the evaluate cli.  This is an end-to-end test, so doesn't need to try
    to explore all edge cases.  For more specific tests, it's better to write
    evaluation tests.

    """
    input_data_path = get_fixture_path("input_data")
    input_artifact_path = get_fixture_path("artifact")
