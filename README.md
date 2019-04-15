# Microcosm Service Cookie Cutter

Project template for a `microcosm`-based ML service using SageMaker.

## Usage

 1. Install [cookiecutter](https://github.com/audreyr/cookiecutter):

        pip install cookiecutter

 2. Change to an appropriate working directory.

 3. Run cookiecutter against this repository:

        cookiecutter https://github.com/globality-corp/cookiecutter-microcosm-sagemaker

 4. Answer the questions. Be sure to provide an appropriate value for the
    `repository_name`.  By convention, all ML repositories should be prefixed
    with `ml-`, and all NLP repositories should be prefixed with `ml-nlp-`.

 5. Change into the `{{ repository_name }}` directory and initialize a new git project from there:

        git init
        git add .
        git commit -m "Initial commit"


## Development

The `scripts/instantiate.sh` script is useful during development.  It will
instantiate the cookiecutter with default parameters, removing any previous
instantiations.  You can then cd into the instantiated directory to run linting
and unit tests.
