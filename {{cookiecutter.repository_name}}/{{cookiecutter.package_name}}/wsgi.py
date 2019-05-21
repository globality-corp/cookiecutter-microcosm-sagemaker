"""
Entrypoint module for WSGI containers.

"""
from microcosm_sagemaker.artifact import InputArtifact
from microcosm_sagemaker.constants import SagemakerPath

from {{ cookiecutter.package_name }}.app_hooks.serve.app import create_app


graph = create_app()

default_artifact_path = SagemakerPath.MODEL
graph.active_bundle.load(InputArtifact(default_artifact_path))

app = graph.app
