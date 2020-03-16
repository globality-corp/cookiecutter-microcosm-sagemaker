"""
Configure v1 swagger endpoint.
"""
from microcosm.api import binding
from microcosm_flask.conventions.swagger import SwaggerConvention
from microcosm_flask.namespaces import Namespace


@binding("v1_swagger_convention")
def configure_swagger(graph):
    ns = Namespace(
        subject="swagger",
        version="v1",
    )
    graph.config.swagger_convention.operations.append("command")
    convention = SwaggerConvention(graph)
    convention.configure(ns, discover=tuple())
    return ns.subject