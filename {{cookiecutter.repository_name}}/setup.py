#!/usr/bin/env python
from setuptools import find_packages, setup


project = "{{ cookiecutter.package_name }}"
version = "{{ cookiecutter.project_version }}"

setup(
    name=project,
    version=version,
    description="{{ cookiecutter.short_description }}",
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.author_email }}",
    url="https://github.com/{{ cookiecutter.organization_name }}/{{ cookiecutter.repository_name }}",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "click>=7.0",
        "microcosm-logging>=1.3.0",
        "microcosm-sagemaker>=0.3.0",
        "microcosm-secretsmanager>=1.1.0",
        "microcosm>=2.4.1",
        "pyOpenSSL>=18.0.0",
    ],
    setup_requires=[
        "nose>=1.3.7",
    ],
    entry_points={
        "microcosm_sagemaker.app_hooks": [
            "train = {{ cookiecutter.package_name }}.app_hooks.train.app:create_app",
            "serve = {{ cookiecutter.package_name }}.app_hooks.serve.app:create_app",
            "evaluate = {{ cookiecutter.package_name }}.app_hooks.evaluate.app:create_app",
        ],
    },
    extras_require={
        "test": [
            "coverage>=4.0.3",
            "PyHamcrest>=1.9.0",
        ],
    },
)
