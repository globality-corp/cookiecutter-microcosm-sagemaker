#!/bin/bash -e

# Container entrypoint to simplify running the production and dev servers.

# Entrypoint conventions are as follows:
#
#  -  If the container is run without a custom CMD, the service should run as it would in production.
#
#  -  If the container is run with the "dev" CMD, the service should run in development mode.
#
#     Normally, this means that if the user's source has been mounted as a volume, the server will
#     restart on code changes and will inject extra debugging/diagnostics.
#
#  -  If the CMD is "test" or "lint", the service should run its unit tests or linting.
#
#     There is no requirement that unit tests work unless user source has been mounted as a volume;
#     test code should not normally be shipped with production images.
#
#  -  Otherwise, the CMD should be run verbatim.


if [ "$1" = "uwsgi" ]; then
    exec uwsgi --http-socket 0.0.0.0:80 \
        --drop-after-init \
        --uid nobody \
        --gid nogroup \
        --disable-logging \
        --processes ${UWSGI_NUM_PROCESSES:-4} \
        --need-app --module ${NAME}.wsgi:app
elif [ "$1" = "dev" ]; then
    exec runserver --host 0.0.0.0 --port 80
elif [ "$1" = "migrate" ]; then
    echo "No command for migrate entrypoint"
elif [ "$1" = "test" ]; then
    # Install standard test dependencies; YMMV
    pip --quiet install \
        --extra-index-url $EXTRA_INDEX_URL \
        .[test] nose "PyHamcrest<1.10.0" coverage
    exec nosetests ${NAME} --exclude api_contract_test
elif [ "$1" = "api-contract-test" ]; then
    pip --quiet install \
        --extra-index-url $EXTRA_INDEX_URL \
        .[test] nose "PyHamcrest<1.10.0"
    if [[ -d "${NAME}/tests/api_contract_test" ]]
    then
        exec nosetests ${NAME}/tests/api_contract_test
    else
        echo "No API contract tests to run"
    fi
elif [ "$1" = "lint" ]; then
    # Install standard linting dependencies; YMMV
    pip --quiet install \
        --extra-index-url $EXTRA_INDEX_URL \
        .[lint] flake8 flake8-print flake8-logging-format flake8-isort
    exec flake8 ${NAME}
elif [ "$1" = "typehinting" ]; then
    # Install standard type-linting dependencies
    pip --quiet install mypy
    exec mypy ${NAME} --ignore-missing-imports
elif [ "$1" = "test-artifact" ]; then
    echo "starting test-artifact..."
    pip install awscli
    echo "starting to copy model..."
    echo $MODEL_LOCATION
    aws s3 cp ${MODEL_LOCATION} .
    mkdir -p /opt/ml/model
    tar -zxf model.tar.gz -C /opt/ml/model
    mkdir -p /opt/ml/input/data/test
    echo "starting to sync test dataset..."
    echo $TEST_DATASET_LOCATION
    aws s3 cp --recursive ${TEST_DATASET_LOCATION} /opt/ml/input/data/test
    # Install standard test dependencies; YMMV
    pip --quiet install \
        --extra-index-url $EXTRA_INDEX_URL \
        .[test] nose PyHamcrest coverage
    exec nosetests ${NAME} --attr 'requires_artifact'
else
    exec "$@"
fi
