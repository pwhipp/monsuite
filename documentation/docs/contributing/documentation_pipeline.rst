Documentation Pipeline
======================

Read the docs
-------------

Current deployment is to `read the docs`_. Pushes to the git hub repository should automagically update the
documentation which can be seen at `monsuite.readthedocs.io <http://monsuite.readthedocs.io/>`_ or at
`monsuite.rtfd.io <http://monsuite.rtfd.io/>`_.

Local Live Reload
-----------------

To avoid delays when reviewing changes as you make them locally, use livereload (included in requirements):

Once you've cloned the repo on mac or linux execute `python live.py <port>` in the root folder. The port will default to
5500 if not supplied.

.. _read the docs: https://docs.readthedocs.io/en/latest/builds.html