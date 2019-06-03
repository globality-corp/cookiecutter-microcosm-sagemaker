from hamcrest import contains, has_properties
from microcosm_sagemaker.testing.bundle import (
    BundleFitTestCase,
    BundleLoadTestCase,
    BundlePredictionCheck,
    BundleSaveTestCase,
    BundleTestCase,
)

from {{ cookiecutter.package_name }}.tests.fixtures import get_fixture_path


class ExampleBundleTestCase(BundleTestCase):
    """
    All of the test cases in this file will be testing example bundle, and use
    the same root input artifact.  They will also check the bundle prediction
    in the same way when necessary.  Thus, we define these parameters in a base
    class here.

    """

    # Determines which bundle will be tested
    bundle_name = "example_bundle"

    # Contains a full root input artifact that will be used to automatically
    # load all dependency bundles and, for the load test, to test loading of
    # the bundle under test
    root_input_artifact_path = get_fixture_path("example_input_artifact")

    # After fit / load, the following sets of args / kwargs / return value
    # matchers will be used to check that the bundle.predict member function
    # works as expected.
    bundle_prediction_checks = [
        BundlePredictionCheck(
            args=[1.0],
            return_value_matcher=contains(
                has_properties(
                    uri="http://example.com",
                    score=3.0,
                ),
            )
        )
    ]


class TestExampleBundleFit(BundleFitTestCase, ExampleBundleTestCase):
    """
    We just need to provide the location of a small test dataset.  This dataset
    will be used to fit the bundle, and then the prediction will be tested
    using the `check_bundle_prediction` function defined above.

    """
    input_data_path = get_fixture_path("example_input_data")


class TestExampleBundleSave(BundleSaveTestCase, ExampleBundleTestCase):
    """
    In this case the bundle and all its dependencies will first be loaded, and
    then the bundle under test will be saved.  We only need to provide the
    location of a gold bundle output artifact that the bundle's saved artifact
    will be checked against.

    If necessary, `output_artifact_matchers` can be defined to customize the
    way files are compared between gold artifact and actual artifact.

    """
    gold_bundle_output_artifact_path = (
        get_fixture_path("example_gold_output_artifact") / "example_bundle"
    )


class TestExampleBundleLoad(BundleLoadTestCase, ExampleBundleTestCase):
    """
    In this case, we just need the root input artifact defined above, and the
    correct bundle artifact will automatically be discovered.  The load
    function of `example_bundle` will be exercised using this artifact.

    """
    pass
