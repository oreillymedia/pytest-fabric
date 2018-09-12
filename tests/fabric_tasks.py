from fabric.api import task, run


@task
def create_readme():
    run('echo "This is a new README" >> /tmp/README.rst')
