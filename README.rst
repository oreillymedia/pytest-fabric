pytest-fabric

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

::

from mytasks import task

def test_fabric_task(fabric_host):
    execute(task)


Note: pytest-capture does not like when we try to actually write to stdout like in fabric so make sure to add ``-s`` to your pytest args