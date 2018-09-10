from fabric.api import execute

from .fabric_tasks import create_readme


def test_fabric_task_executes(fabric_host):
    execute(create_readme)
    ls_results = fabric_host.exec_run('ls /tmp/')
    assert ls_results[1].strip() == 'README.rst'
