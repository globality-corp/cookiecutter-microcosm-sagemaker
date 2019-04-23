# {{cookiecutter.project_name}}

{{cookiecutter.short_description}}


## Developing

To setup the project for local development, make sure you have a virtualenv setup, and then run:

    pip install -e .

This will install all the dependencies and set the project up for local usage.


### Directory structure

- `bundles/`: Contains the bundles.  Each bundle wraps an ML model and also
  handles the setup and data transformation around the given model.
- `app_hooks/`: Contains the `app` and `config` information for use by the CLI
  commands defined in `microcosm-sagemaker`.
- `evaluations/`: Evaluation metrics
- `data_models/`: These are data models, **not** ML models.  Note that in
  standard microcosm services, this directory would be called `models/`, but to
  avoid confusion with the ML term, we use the more explicit `data_models/`
  here.
- `resources/`: REST resources
- `routes/`: REST routes
- `tests/`: Tests


## Training

To train on a dataset locally, run

    train

To see supported arguments, run

    train --help

You can also train on SageMaker using the
[`globality-ml-scripts`](https://github.com/globality-corp/globality-ml-scripts)
CLI.

## Flask

To run the Flask web server when developing locally, invoke the following:

    runserver

The service publishes two endpoints, as expected by SageMaker:

 -  The service supports SageMaker's ping endpoint:

        GET /ping

 -  The service supports invocations:

        POST /invocations
