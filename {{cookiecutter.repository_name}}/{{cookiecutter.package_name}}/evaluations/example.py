from microcosm.api import binding, defaults
from microcosm_logging.decorators import logger
from microcosm_sagemaker.bundle import Bundle
from microcosm_sagemaker.evaluation import Evaluation
from microcosm_sagemaker.input_data import InputData


@binding("example_evaluation")
@defaults(
    example_param=1.0,
)
@logger
class ExampleEvaluation(Evaluation):
    def __init__(self, graph):
        config = graph.config.example_bundle

        self.example_param = config.example_param

    def __call__(self, bundle: Bundle, input_data: InputData):
        self.logger.info(
            f"Running example_evaluation on bundle {bundle} with input "
            f"{input_data.path} and param {self.example_param}"
        )
