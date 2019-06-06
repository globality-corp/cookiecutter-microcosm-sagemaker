#!/usr/bin/env python
from cookiecutter.main import cookiecutter


cookiecutter(
    '.',
    no_input=True,
    extra_context=dict(
        repository_name="cookiecutter-microcosm-sagemaker",
    )
)
