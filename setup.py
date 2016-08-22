#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="pytoolkit",
    version="2016.8.0",
    description="Asorted tools, not ready for general use.",
    author="pnc",
    license="BSD",
    author_email="no@spam.please",
    url="https://github.com/poncki/pytoolkit",
    keywords=[],
    include_package_data=True,
    zip_safe=False,

    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(where="src", exclude=["tests", ".__stash__"]),
    package_dir={"": "src"},
    # py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    install_requires=[
        "click",
    ],
    extras_require={
        # eg:
        #   "rst": ["docutils>=0.11"],
        #   ":python_version=="2.6"": ["argparse"],
    },
    tests_require=[
        "pytest",
        "pytest-cov",
    ],
    test_suite="tests",

    entry_points={
        "console_scripts": [
            "ptk = pytoolkit.cli:main",
        ]
    },
)
