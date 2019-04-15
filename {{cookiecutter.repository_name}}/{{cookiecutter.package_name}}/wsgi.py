"""
Entrypoint module for WSGI containers.

"""
from {{ cookiecutter.package_name }}.commands.serve.app import create_app


app = create_app().app
