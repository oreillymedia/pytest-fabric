"""A pytest plugin which helps testing Django applications
This plugin handles creating and destroying the test environment and
test database and provides some useful text fixtures.
"""

from .fixtures import docker_client, fabric_host # noqa
