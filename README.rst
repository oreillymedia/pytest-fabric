pytest-fabric
-------------

.. image:: https://travis-ci.org/efagerberg/pytest-fabric.svg?branch=master
    :target: https://travis-ci.org/efagerberg/pytest-fabric


Requirements
============

- Python 2.7
- Fabric 1.14.0


TODOs (will make into issues eventually)
========================================

* Only runs one host right now if using `fabric_host` fixture (Support multiple container)


Usage
=====

``fabric_host`` will set up the fabric environment to be SSHable
The object is a `docker.models.containers.Container` object.

From here, users should be able to exec into the container to check
things like the image files and such.

Note: This should work for docker-machine or docker

.. code:: python

    from fabric.api import execute

    from .fabric_tasks import create_readme


    def test_fabric_task_executes(fabric_host):
        execute(create_readme)
        ls_results = fabric_host.exec_run('ls /tmp/')
        assert ls_results[1].strip() == 'README.rst'


Note: pytest-capture does not like when we try to actually write to stdout like in fabric so make sure to add ``-s`` to your pytest args
