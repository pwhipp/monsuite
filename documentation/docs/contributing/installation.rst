Installation
============

Installation is only required if you wish to work on your own local copy of the project. If you are only changing the documentation content, it is posible to work entirely through github.

Install pip
...........

NOTE: PIP is used to conveniently install Python modules needed for the project. If 'which pip' returns a path to pip, it is already installed. If it is not installed, follow these instructions:

get 'distribute_setup.py':

.. code::

   ~ $ sudo apt-get install python3-pip

verify `pip`:

.. code::

   ~ $ which pip3
   /usr/bin/pip3

Set up Virtualenvwrapper
........................

[Install `virtualenwrapper`](http://virtualenvwrapper.readthedocs.org/en/latest/install.html) with `sudo`.

Create a new virtual environment and work within it

.. note::

   Use pip3 rather than pip to install mkvirtualenvwrapper if you have an old python (<2.7) as the default on your OS.

.. code::

   ~ $ mkvirtualenv sosadmin  --python /usr/bin/python3

You can name the virtualenv whatever you like, just be sure to adapt the remaining instructions appropriately.

.. note::

   If the `mkvirtualenv` returns a "command not found" error, follow these steps:

   - check that 'virtualenvwrapper.sh' is in `/usr/local/bin`
   - assuming that it is, use the `source` command to pass the contents of 'virtualenvwrapper.sh'to the Tcl interpreter: source /usr/local/bin/virtualenvwrapper.sh
   - verify that this works by re-running the virtualenv command:

   .. code::

      ~ $ mkvirtualenv sosadmin  --python /usr/bin/python3

   - exit virtualenv and `echo` the `source` command into the local user's `.bashrc`:

   .. code::

      ~ $ deactivate
      ~ $ echo 'source /usr/local/bin/virtualenvwrapper.sh' >> .bashrc

.. _clone:

Clone the repository and install the requirements
-------------------------------------------------

.. code::

   (sosadmin)~ $ git clone git@sos.cliosoft.net:sosadmin.git
   (sosadmin)~ $ cd sosadmin
   (sosadmin)~/sosadmin $ pip install -r requirements.txt

This installs Django and the other required Python modules.

Set up the virtual environment
------------------------------

These commands assume the settings and virtualenv - edit them as necessary.

.. code::

   (sosadmin)~/sosadmin $ add2virtualenv .
   (sosadmin)~/sosadmin $ setvirtualenvproject
   (sosadmin)~/sosadmin $ echo "export DJANGO_SETTINGS_MODULE=core.settings.dev" >> ~/.virtualenvs/sosadmin/bin/postactivate
   (sosadmin)~/sosadmin $ deactivate
   ~/sosadmin $ workon sosadmin
   (sosadmin)~/sosadmin $