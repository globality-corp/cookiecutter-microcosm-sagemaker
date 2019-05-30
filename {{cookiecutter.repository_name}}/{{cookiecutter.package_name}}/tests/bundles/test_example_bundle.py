from hamcrest import assert_that, contains, has_properties

from microcosm_sagemaker.testing.bundle import (
    BundleFitTestCase,
    BundleLoadTestCase,
    BundleSaveTestCase,
    BundleTestCase,
)

from {{ cookiecutter.package_name }}.bundles.example import ExampleBundle
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

    # This function will be called on the bundle after fitting / loading to
    # make sure it works correctly
    def check_bundle_prediction(self, bundle: ExampleBundle) -> None:
        assert_that(
            bundle.predict(1.0),
            contains(has_properties(
                uri="http://example.com",
                score=3.0,
            )),
        )


class TestExampleBundleFit(BundleFitTestCase, ExampleBundleTestCase):
    """
    We just need to provide the location of a dataset that we will fit and then
    the fit bundle will be checked using the prediction checker above.

    """
    input_data_path = get_fixture_path("example_input_data")


class TestExampleBundleSave(BundleSaveTestCase, ExampleBundleTestCase):
    """
    In this case the bundle and all its dependencies will be loaded, and then
    the bundle under test will be saved.  We provide the location of a gold
    bundle output artifact that the bundle's saved artifact will be checked
    against.

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
