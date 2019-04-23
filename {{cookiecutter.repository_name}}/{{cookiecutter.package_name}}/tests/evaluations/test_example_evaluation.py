from microcosm_sagemaker.artifact import InputArtifact
from microcosm_sagemaker.input_data import InputData

from {{ cookiecutter.package_name }}.app_hooks.train.app import create_app
from {{ cookiecutter.package_name }}.tests.fixtures import get_fixture_path


class TestExampleEvaluation:
    def setup(self) -> None:
        self.graph = create_app(extra_deps=["example_evaluation"])

        self.input_data = InputData(get_fixture_path("example_input_data"))
        self.input_artifact = InputArtifact(get_fixture_path("example_input_artifact"))

    def test_evaluation(self) -> None:
        bundle = self.graph.active_bundle
        bundle.load(self.input_artifact)

        self.graph.example_evaluation(bundle, self.input_data)
