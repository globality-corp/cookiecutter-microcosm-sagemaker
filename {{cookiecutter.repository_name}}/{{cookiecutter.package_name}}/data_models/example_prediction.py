from dataclasses import dataclass


@dataclass
class ExamplePrediction:
    uri: str
    score: float
