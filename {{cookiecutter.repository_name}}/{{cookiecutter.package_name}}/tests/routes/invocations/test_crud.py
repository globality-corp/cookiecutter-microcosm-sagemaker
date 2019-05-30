"""
Example CRUD routes tests.

Tests are sunny day cases under the assumption that framework conventions
handle most error conditions.

"""
from hamcrest import contains, has_entries
from microcosm_sagemaker.testing.invocations import InvocationsRouteTestCase

from {{cookiecutter.package_name}}.tests.fixtures import get_fixture_path


class TestInvocationsRoute(InvocationsRouteTestCase):
    """
    Tests the invocations route.  This is an end-to-end test, so doesn't need
    to try to explore all edge cases.  For more specific tests, it's better to
    write bundle tests.

    """
    # Path to a trained artifact that will be loaded prior to invoking the
    # invocations route
    root_input_artifact_path = get_fixture_path("example_input_artifact")

    # Some request json to test the route with
    request_json = dict(exampleArg=1.0)

    # A matcher that the `items` of the response will be checked against
    response_items_matcher = contains(
        has_entries(
            uri="http://example.com",
            score=3.0,
        ),
    )
