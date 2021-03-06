.. readthedocs_test documentation master file, created by
   sphinx-quickstart on Sun Aug 20 09:14:50 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to readthedocs_test's documentation!
============================================

This is a test of using Sphinx(+breathe) to generate automatic documentation from comments in both `python`, `c++`, and `fortran` code in a mixed project.

The documentation can be automatically generated and hosted by http://readthedocs.org/ if the git repository of the code https://github.com/HugoStrand/readthedocs_test is linked to their service.

Building the documentation locally requires
-------------------------------------------

- `CMake` https://cmake.org/
- `sphinx` http://www.sphinx-doc.org/
- `doxygen` http://www.doxygen.org/
- `breathe` http://breathe.readthedocs.io/
- `sphinx_rtd_theme` https://www.github.com/snide/sphinx_rtd_theme

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   pyfoobar.rst
   nutshell.rst
   utils.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
