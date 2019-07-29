from setuptools import setup

setup(
    name="gameoflife",
    version="1.1.0",
    description="Conway's Game of Life Clone",
    url="https://github.com/imanmtj/game-of-life",
    author="imanmtj",
    author_email="iman.montajabi@gamil.com",
    license="GPL-3.0",
    packages=["gameoflife"],
    zip_safe=[False],
    install_requires=["pygame"]
)
