# Microcosm Service Cookie Cutter

Project template for a `microcosm`-based ML service using SageMaker.

## Usage

 1. Install [cookiecutter](https://github.com/audreyr/cookiecutter):

        pip install cookiecutter

 1. Change to an appropriate working directory.

 1. Run cookiecutter against this repository:

        cookiecutter https://github.com/globality-corp/cookiecutter-microcosm-sagemaker

 1. Answer the questions. 

 1. Change into the `{{ repository_name }}` directory

 1. *[Globality only]* Run the `globality-build`
    [setup steps](https://github.com/globality-corp/globality-build#usage-template-generation).
 
 1. Initialize a new git project:

        git init
        git add .
        git commit -m "Initial commit"


## Cookiecutter development

When experimenting with changes to this cookiecutter, you may find the
`scripts/instantiate.sh` script to be useful.  It will instantiate the
cookiecutter with the default parameters, first removing any previous
instantiations. You can then cd into the instantiated directory to run linting
and unit tests.

Below describes one possible local development flow.

### Setup
Open two shells. In the first shell, no virtualenv is active, and the cwd is
the top level of this cookiecutter repo.  Run

    ./scripts/instantiate.sh

In the second shell,

    cd ml-papaya-extractor
    pyenv virtualenv 3.7.2 ml-papaya-extractor
    pyenv shell ml-papaya-extractor
    pip install flake8 flake8-print flake8-logging-format flake8-isort flake8-quotes mypy

### Development
During development, make all changes to the cookiecutter template, not to the
instantiated test directory.  Then every time you'd like to test a change, in
the first shell, run

    ./scripts/instantiate.sh

Then in the second shell, to run unit tests, run

    cd .. && cd ml-papaya-extractor && pip install -e '.[test]' && python setup.py nosetests

The initial `cd` commands are because the `instantiate` step above clobbers the
`ml-papaya-extractor` directory.

Similarly, to run linting, run

    cd .. && cd ml-papaya-extractor && flake8 .
