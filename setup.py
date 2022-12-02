from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="RlGlue-andnp",
    url="https://github.com/andnp/RlGlue.git",
    author="Andy Patterson",
    author_email="andnpatterson@gmail.com",
    packages=find_packages(exclude=["tests*"]),
    package_data={"RlGlue": ["py.typed"]},
    version="1.0.0",
    license="MIT",
    description="A tiny re-implementation of the rl-glue interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    install_requires=[],
    extras_require={
        "dev": [
            "numpy>=1.19.5",
            "flake8",
            "commitizen",
            "pre-commit",
            "pipenv-setup[black]",
            "build",
            "twine",
            "mypy",
        ],
    },
)
