import tempfile
from pathlib import Path

from hamcrest import assert_that, contains, has_properties
from microcosm_sagemaker.artifact import RootInputArtifact, RootOutputArtifact
from microcosm_sagemaker.input_data import InputData
from microcosm_sagemaker.testing.directory_comparison import (
    directory_comparison,
)

from {{cookiecutter.package_name}}.app_hooks.train.app import create_app
from {{cookiecutter.package_name}}.tests.fixtures import get_fixture_path


class TestExampleBundle:
    def setup(self) -> None:
        self.graph = create_app()
        self.training_initializers = self.graph.training_initializers

        self.input_data = InputData(get_fixture_path("example_input_data"))
        self.input_artifact = RootInputArtifact(get_fixture_path("example_input_artifact"))
        self.gold_output_artifact_path = get_fixture_path("example_gold_output_artifact")

    def check_bundle_prediction(self) -> None:
        assert_that(
            self.graph.example_bundle.predict(1.0),
            contains(has_properties(
                uri="http://example.com",
                score=3.0,
            )),
        )

    def test_fit(self) -> None:
        self.training_initializers.init()
        self.graph.example_bundle.fit(self.input_data)
        self.check_bundle_prediction()

    def test_load(self) -> None:
        self.graph.example_bundle.load(self.input_artifact / "example_bundle")
        self.check_bundle_prediction()

    def test_save(self) -> None:
        self.graph.example_bundle.load(self.input_artifact / "example_bundle")

        with tempfile.TemporaryDirectory() as output_artifact_path:
            output_artifact = RootOutputArtifact(output_artifact_path)
            output_bundle_path = output_artifact / "example_bundle"

            output_bundle_path.path.mkdir()

            self.graph.example_bundle.save(output_bundle_path)

            directory_comparison(
                gold_dir=self.gold_output_artifact_path,
                actual_dir=Path(output_artifact_path),
            )
