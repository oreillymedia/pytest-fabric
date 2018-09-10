from docker.models.containers import Container
from fabric.api import env
from mock import patch

from pytest_fabric.fixtures import get_docker_host


def test_container_fixture_creates_container(docker_client, fabric_host):
    assert isinstance(fabric_host, Container)
    assert fabric_host.image.tags[0] == 'efagerberg/pytest-fabric-sshd:latest'
    assert fabric_host.name == 'pytest-fabric-test-container'
    assert fabric_host.status == 'created'
    inspection_data = docker_client.api.inspect_container(fabric_host.id)
    port_data = inspection_data['NetworkSettings']['Ports']
    assert '22/tcp' in port_data.keys()
    assert port_data['22/tcp'][0]['HostPort'] == '2222'


def test_container_sets_fabric_env_expectedly(docker_client, fabric_host):
    assert env.disable_known_hosts is True
    assert env.hosts == ['root@{}:2222'.format(get_docker_host())]


@patch('pytest_fabric.fixtures.subprocess.Popen.communicate')
def test_get_docker_host_docker_machine(mock_communicate):
    mock_communicate.side_effect = [('192.168.99.100\n', None)]
    assert get_docker_host() == '192.168.99.100'


@patch('pytest_fabric.fixtures.subprocess.Popen.communicate')
def test_get_docker_host(mock_communicate):
    mock_communicate.side_effect = [('', None)]
    assert get_docker_host() == 'localhost'
