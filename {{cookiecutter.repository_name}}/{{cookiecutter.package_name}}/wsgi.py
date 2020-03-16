"""
Entrypoint module for WSGI containers.

"""
from {{cookiecutter.package_name}}.app_hooks.serve.app import create_app


app = create_app().app
