try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

desc = """
=======
RoPaSci
=======

RoPaSci (pronounced ROPE-ASS-KEY) is an interactive Rock, Paper, Scissors game
allowing play against another user or the computer. There are also options for
tournament play and custom rules.
"""

setup(name="RoPaSci",
        version="0.1.0",
        author="Sean Marshallsay",
        author_email="srm.1708@gmail.com",
        url="",
        description="An interactive Rock, Papaer, Scissors game.",
        long_description=desc,
        download_url="",
        packages=["ropasci"],
        scripts=["bin/ropasci"]
)
