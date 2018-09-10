import os
import subprocess

import docker
from fabric.api import env
import pytest


@pytest.fixture()
def docker_client():
    yield docker.from_env()


@pytest.fixture()
def fabric_host(docker_client):
    """Keep this session scoped to save time"""
    container = docker_client.containers.run(
        "efagerberg/pytest-fabric-sshd:latest",
        name="pytest-fabric-test-container",
        ports={'22': '2222'},
        detach=True,
    )
    env.disable_known_hosts = True
    env.password = 'root'
    env.hosts.append('root@{}:2222'.format(get_docker_host()))

    yield container

    container.stop()
    container.remove()
    env.disable_known_hosts = True
    env.hosts = []
    env.password = None


def get_docker_host():
    p = subprocess.Popen(
        ["docker-machine", "ip"],
        stdout=subprocess.PIPE,
        stderr=open(os.devnull, 'w'),
        shell=True)
    docker_machine_host = p.communicate()[0]
    return docker_machine_host.strip() or 'localhost'
