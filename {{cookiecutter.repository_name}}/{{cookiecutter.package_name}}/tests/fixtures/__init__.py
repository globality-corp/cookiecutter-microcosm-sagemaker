from pathlib import Path
from pkg_resources import resource_filename


def get_fixture_path(fixture_name):
    return Path(
        resource_filename(
            '{{ cookiecutter.package_name }}.tests.fixtures',
            fixture_name,
        )
    )
