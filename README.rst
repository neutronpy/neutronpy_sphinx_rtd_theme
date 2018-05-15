
**************************
Read the Docs Sphinx Theme
**************************


Via package
-----------

Download the package or add it to your ``requirements.txt`` file:

.. code:: bash

    $ pip install neutronpy_sphinx_rtd_theme

In your ``conf.py`` file:

.. code:: python

    import sphinx_rtd_theme

    html_theme = "neutronpy_sphinx_rtd_theme"

    html_theme_path = [neutronpy_sphinx_rtd_theme.get_html_theme_path()]

Via git or download
-------------------

Symlink or subtree the ``neutronpy_sphinx_rtd_theme/neutronpy_sphinx_rtd_theme`` repository into your documentation at
``docs/_themes/neutronpy_sphinx_rtd_theme`` then add the following two settings to your Sphinx
conf.py file:

.. code:: python

    html_theme = "neutronpy_sphinx_rtd_theme"
    html_theme_path = ["_themes", ]

Changelog
=========

v0.1.9
------

* Intermittent scrollbar visibility bug fixed. This change introduces a
  backwards incompatible change to the theme's layout HTML. This should only be
  a problem for derivative themes that have overridden styling of nav elements
  using direct decendant selectors. See `#215`_ for more information.
* Safari overscroll bug fixed
* Version added to the nav header
* Revision id was added to the documentation footer if you are using RTD
* An extra block, ``extrafooter`` was added to allow extra content in the
  document footer block
* Fixed modernizr URL
* Small display style changes on code blocks, figure captions, and nav elements

.. _#215: https://github.com/neutronpy/neutronpy_sphinx_rtd_theme/pull/215

v0.1.8
------

* Start keeping changelog :)
* Support for third and fourth level headers in the sidebar
* Add support for Sphinx 1.3
* Add sidebar headers for :caption: in Sphinx toctree
* Clean up sidebar scrolling behavior so it never scrolls out of view

How the Table of Contents builds
================================

Currently the left menu will build based upon any ``toctree(s)`` defined in your index.rst file.
It outputs 2 levels of depth, which should give your visitors a high level of access to your
docs. If no toctrees are set the theme reverts to sphinx's usual local toctree.

It's important to note that if you don't follow the same styling for your rST headers across
your documents, the toctree will misbuild, and the resulting menu might not show the correct
depth when it renders.

Also note that the table of contents is set with ``includehidden=true``. This allows you
to set a hidden toc in your index file with the hidden_ property that will allow you
to build a toc without it rendering in your index.

By default, the navigation will "stick" to the screen as you scroll. However if your toc
is vertically too large, it will revert to static positioning. To disable the sticky nav
altogether change the setting in ``conf.py``.

Contributing or modifying the theme
===================================

The sphinx_rtd_theme is primarily a sass_ project that requires a few other sass libraries. I'm
using bower_ to manage these dependencies and sass_ to build the css. The good news is
I have a very nice set of grunt_ operations that will not only load these dependencies, but watch
for changes, rebuild the sphinx demo docs and build a distributable version of the theme.
The bad news is this means you'll need to set up your environment similar to that
of a front-end developer (vs. that of a python developer). That means installing node and ruby.

Set up your environment
-----------------------

1. Install sphinx_ into a virtual environment.

.. code::

    pip install sphinx

2. Install sass

.. code::

    gem install sass

2. Install node, bower and grunt.

.. code::

    // Install node
    brew install node

    // Install bower and grunt
    npm install -g bower grunt-cli

    // Now that everything is installed, let's install the theme dependecies.
    npm install

Now that our environment is set up, make sure you're in your virtual environment, go to
this repository in your terminal and run grunt:

.. code::

    grunt

This default task will do the following **very cool things that make it worth the trouble**.

1. It'll install and update any bower dependencies.
2. It'll run sphinx and build new docs.
3. It'll watch for changes to the sass files and build css from the changes.
4. It'll rebuild the sphinx docs anytime it notices a change to .rst, .html, .js
   or .css files.
=======
.. image:: https://img.shields.io/pypi/v/sphinx_rtd_theme.svg
   :target: https://pypi.python.org/pypi/sphinx_rtd_theme
   :alt: Pypi Version 
.. image:: https://travis-ci.org/rtfd/sphinx_rtd_theme.svg?branch=master
   :target: https://travis-ci.org/rtfd/sphinx_rtd_theme
   :alt: Build Status
.. image:: https://img.shields.io/pypi/l/sphinx_rtd_theme.svg
   :target: https://pypi.python.org/pypi/sphinx_rtd_theme/
   :alt: License
.. image:: https://readthedocs.org/projects/sphinx-rtd-theme/badge/?version=latest
  :target: http://sphinx-rtd-theme.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

The ``sphinx_rtd_theme`` is a sphinx_ theme designed to look modern and be mobile-friendly.
This theme is primary focused to be used on readthedocs.org_ but can work with your
own sphinx projects. To read more and see a working demo_ head over to readthedocs.org_.

.. _sphinx: http://www.sphinx-doc.org
.. _readthedocs.org: http://www.readthedocs.org
.. _demo: https://sphinx-rtd-theme.readthedocs.io/en/latest/


Installing
==========

The theme is distributed on PyPI_ and can be installed with pip::

   pip install sphinx_rtd_theme

For more information read the full installing docs
`here <https://sphinx-rtd-theme.readthedocs.io/en/latest/installing.html>`__.

.. _PyPI: https://pypi.python.org/pypi/sphinx_rtd_theme


Configuration
=============

The ``sphinx_rtd_theme`` is highly customizable on both the page level and on a global level.
To see all the possible configuration options read the configuring docs
`here <https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html>`__.


Contributing
============

If you would like to help improve the theme or have more control
over the theme in case of a fork please read our contributing guide
`here <https://sphinx-rtd-theme.readthedocs.io/en/latest/contributing.html>`__.
