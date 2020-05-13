from typing import List

from microcosm.api import binding, defaults
from microcosm_logging.decorators import logger
from microcosm_sagemaker.artifact import BundleInputArtifact, BundleOutputArtifact
from microcosm_sagemaker.bundle import Bundle
from microcosm_sagemaker.input_data import InputData

from {{cookiecutter.package_name}}.data_models.example_prediction import ExamplePrediction


@binding("example_bundle")
@defaults(
    example_param=1.0,
)
@logger
class ExampleBundle(Bundle):
    def __init__(self, graph):
        config = graph.config.example_bundle

        self.example_param = config.example_param

    @property
    def dependencies(self) -> List[Bundle]:
        """
        List of bundles upon which this bundle depends.  Whenever the `fit`,
        `save` or `load` methods are called on this bundle, it is guaranteed
        that the corresponding methods will have first been called on all
        `dependency` bundles.

        This example bundle has no dependencies.

        """
        return []

    def fit(self, input_data: InputData) -> None:
        """
        Perform training

        For this example, we just expect the input dataset to contain a file
        with a number in it, and we store that as our trained param.

        """
        self.logger.info(
            f"Fitting example_bundle with input {input_data.path} "
            f"and param {self.example_param}"
        )

        with open(input_data.path / "example.txt") as input_file:
            self.example_trained_param = float(input_file.read())

    def predict(self, example_arg: float) -> List[ExamplePrediction]:
        """
        Predict using the trained model.

        For this example, we just add the configured param, the learned param,
        and the argument in order to demonstrate how to use all three.

        """
        return [
            ExamplePrediction(
                uri="http://example.com",
                score=(
                    self.example_param +
                    self.example_trained_param +
                    example_arg
                ),
            ),
        ]

    def save(self, output_artifact: BundleOutputArtifact) -> None:
        """
        Save the trained model

        For this example, we just store the param we read during training.

        """
        self.logger.info(
            f"Saving example_bundle to {output_artifact.path}"
        )

        # Save the trained model
        # For this example, we just store the param we read during training
        with open(output_artifact.path / "example.txt", "w") as output_file:
            output_file.write(str(self.example_trained_param))

    def load(self, input_artifact: BundleInputArtifact) -> None:
        """
        Load the trained model

        For this example, we just load the param we stored during save.

        """
        self.logger.info(
            f"Loading from {input_artifact.path}"
        )

        with open(input_artifact.path / "example.txt") as input_file:
            self.example_trained_param = float(input_file.read())
