============
arithmetical
============

Class for representing arithmetic operators as callable, immutable, hashable, and sortable objects.

|pypi| |readthedocs| |actions| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/arithmetical.svg
   :target: https://badge.fury.io/py/arithmetical
   :alt: PyPI version and link.

.. |readthedocs| image:: https://readthedocs.org/projects/arithmetical/badge/?version=latest
   :target: https://arithmetical.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs documentation status.

.. |actions| image:: https://github.com/reity/arithmetical/workflows/lint-test-cover-docs/badge.svg
   :target: https://github.com/reity/arithmetical/actions/workflows/lint-test-cover-docs.yml
   :alt: GitHub Actions status.

.. |coveralls| image:: https://coveralls.io/repos/github/reity/arithmetical/badge.svg?branch=main
   :target: https://coveralls.io/github/reity/arithmetical?branch=main
   :alt: Coveralls test coverage summary.

Installation and Usage
----------------------
This library is available as a `package on PyPI <https://pypi.org/project/arithmetical>`__::

    python -m pip install arithmetical

The library can be imported in the usual ways::

    import arithmetical
    from arithmetical import *

Examples
^^^^^^^^

.. |arithmetical| replace:: ``arithmetical``
.. _arithmetical: https://arithmetical.readthedocs.io/en/0.1.0/_source/arithmetical.html#arithmetical.arithmetical.arithmetical

.. |operator| replace:: ``operator``
.. _operator: https://docs.python.org/3/library/operator.html#module-operator

Each instance of the |arithmetical|_ class (derived from the type of the built-in functions found in the built-in :obj:`operator` library) represents a function that operates on on values of `numeric <https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex>`__ types and on objects that define the `special methods <https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types>`__ associated with these built-in operators.

    >>> from arithmetical import arithmetical
    >>> arithmetical.add_(1, 2)
    3

Methods for retrieving the name and arity of an |arithmetical|_ instance are provided.

    >>> arithmetical.add_.name()
    'add'
    >>> arithmetical.add_.arity()
    2

Instances of |arithmetical|_ can be compared according to their precedence.

    >>> arithmetical.pow_ > arithmetical.mul_
    True
    >>> arithmetical.pow_ <= arithmetical.add_
    False
    >>> sorted([pow_, mul_, add_] # From lowest to highest precedence.
    [add_, mul_, pow_]

Instances are also hashable and can be used as members of `sets <https://docs.python.org/3/tutorial/datastructures.html#sets>`__ and as keys within `dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`__.

    >>> from arithmetical import *
    >>> {add_, mul_}
    {mul_, add_}
    >>> {add_: 0, mul_: 1}
    {add_: 0, mul_: 1}

This library is compatible with the `circuit <https://pypi.org/project/circuit>`__ library (and is intended to complement the `logical <https://pypi.org/project/logical>`__ library for logical operations).

Development
-----------
All installation and development dependencies are fully specified in ``pyproject.toml``. The ``project.optional-dependencies`` object is used to `specify optional requirements <https://peps.python.org/pep-0621>`__ for various development tasks. This makes it possible to specify additional options (such as ``docs``, ``lint``, and so on) when performing installation using `pip <https://pypi.org/project/pip>`__::

    python -m pip install .[docs,lint]

Documentation
^^^^^^^^^^^^^
The documentation can be generated automatically from the source files using `Sphinx <https://www.sphinx-doc.org>`__::

    python -m pip install .[docs]
    cd docs
    sphinx-apidoc -f -E --templatedir=_templates -o _source .. && make html

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

Ensure that the correct version number appears in ``pyproject.toml``, and that any links in this README document to the Read the Docs documentation of this package (or its dependencies) have appropriate version numbers. Also ensure that the Read the Docs project for this library has an `automation rule <https://docs.readthedocs.io/en/stable/automation-rules.html>`__ that activates and sets as the default all tagged versions. Create and push a tag for this version (replacing ``?.?.?`` with the version number)::

    git tag ?.?.?
    git push origin ?.?.?

Remove any old build/distribution files. Then, package the source into a distribution archive::

    rm -rf build dist src/*.egg-info
    python -m build --sdist --wheel .

Finally, upload the package distribution archive to `PyPI <https://pypi.org>`__::

    python -m twine upload dist/*
