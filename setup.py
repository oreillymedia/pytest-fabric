import sys
from setuptools import setup, find_packages


setup(
    name='pytest-fabric',
    version='1.0.0',
    description=('Provides test utilities to run fabric task '
                 'tests by using docker containers'),
    long_description=open('README.rst').read(),
    author='Evan Fagerberg',
    author_email='adioevan@gmail.com',
    zip_safe=True,
    url='http://github.com/efagerberg/pytest-fabric',
    license='MIT',
    packages=find_packages(exclude=('tests',)),
    keywords='fabric docker pytest python',
    install_requires=[
        'pytest>=2.9',
        'docker>=3.5.0',
        'fabric==1.14.0',
        'six',
        'mock',
        'pytest-cov',
        'pytest-xdist',
    ],
    setup_requires=['pytest-runner'] if any(x in ('pytest', 'test')
                                            for x in sys.argv) else [],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    # the following makes a plugin available to pytest
    entry_points={'pytest11': ['fabric = pytest_fabric.plugin']})
