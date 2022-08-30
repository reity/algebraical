============
arithmetical
============

Class for representing arithmetic operators as callable, immutable, hashable, and sortable objects.

|pypi|

.. |pypi| image:: https://badge.fury.io/py/arithmetical.svg
   :target: https://badge.fury.io/py/arithmetical
   :alt: PyPI version and link.

Installation and Usage
----------------------
This library is available as a `package on PyPI <https://pypi.org/project/arithmetical>`__::

    python -m pip install arithmetical

The library can be imported in the usual ways::

    import arithmetical
    from arithmetical import *

Development
-----------
All installation and development dependencies are fully specified in ``pyproject.toml``. The ``project.optional-dependencies`` object is used to `specify optional requirements <https://peps.python.org/pep-0621>`__ for various development tasks. This makes it possible to specify additional options (such as ``test``, ``lint``, and so on) when performing installation using `pip <https://pypi.org/project/pip>`__::

    python -m pip install .[test,lint]

Testing and Conventions
^^^^^^^^^^^^^^^^^^^^^^^
All unit tests are executed and their coverage is measured when using `pytest <https://docs.pytest.org>`__ (see the ``pyproject.toml`` file for configuration details)::

    python -m pip install .[test]
    python -m pytest

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`__::

    python src/arithmetical/arithmetical.py -v

Style conventions are enforced using `Pylint <https://pylint.pycqa.org>`__::

    python -m pip install .[lint]
    python -m pylint src/arithmetical

Contributions
^^^^^^^^^^^^^
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/reity/arithmetical>`__ for this library.

Versioning
^^^^^^^^^^
The version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`__.

Publishing
^^^^^^^^^^
This library can be published as a `package on PyPI <https://pypi.org/project/arithmetical>`__ by a package maintainer. First, install the dependencies required for packaging and publishing::

    python -m pip install .[publish]

Remove any old build/distribution files. Then, package the source into a distribution archive::

    rm -rf build dist src/*.egg-info
    python -m build --sdist --wheel .

Finally, upload the package distribution archive to `PyPI <https://pypi.org>`__::

    python -m twine upload dist/*
