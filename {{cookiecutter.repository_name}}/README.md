# {{cookiecutter.project_name}}

{{cookiecutter.short_description}}


## Developing

To setup the project for local development, make sure you have a virtualenv
setup, and then run:

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

To train on a dataset locally, run something like the following:

    train --input-data {{ cookiecutter.package_name }}/tests/fixtures/input_data \
          --output-artifact models/test

To see supported arguments, run

    train --help

You can also train on SageMaker using the
[`globality-ml-scripts`](https://github.com/globality-corp/globality-ml-scripts)
CLI.

## Flask

To run the Flask web server when developing locally, invoke something like the
following:

    runserver --input-artifact models/test

The service publishes several endpoints by default.

 -  The service supports invocations, which are the supported way of doing
    inference:

        POST /api/v1/invocations

 -  The service publishes its own health:

        GET /api/health

 -  The service publishes a [crawlable](https://en.wikipedia.org/wiki/HATEOAS)
    endpoint for discovery of its operations:

        GET /api/

 -  The service publishes [Swagger](http://swagger.io/) definitions for its
    operations (by API version) using
    [HAL JSON](http://stateless.co/hal_specification.html):

        GET /api/v1/swagger