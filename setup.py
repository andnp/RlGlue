from setuptools import setup, find_packages

setup(
    name='RlGlue',
    url='https://github.com/andnp/RlGlue.git',
    author='Andy Patterson',
    author_email='andnpatterson@gmail.com',
    packages=find_packages(exclude=['tests*']),
    install_requires=[],
    version=0.0,
    license='MIT',
    description='A tiny re-implementation of the rl-glue interface',
    long_description='todo',
)
