.. Swauth documentation master file, created by
   sphinx-quickstart on Mon Feb 14 19:34:51 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Swauth
======

    Copyright (c) 2010-2011 OpenStack, LLC

    An Auth Service for Swift as WSGI Middleware that uses Swift itself as a
    backing store. Sphinx-built docs at: http://gholt.github.com/swauth/
    Source available at: https://github.com/gholt/swauth

    See also https://github.com/khussein/keystone for the future standard
    OpenStack auth service.

    This is currently a work in progress of pulling Swauth out of the Swift
    repo and here into its own project. See
    https://code.launchpad.net/~gholt/swift/deswauth/+merge/62392 for the Swift
    side of things.

Quick Install
-------------

1) Install Swauth with ``sudo python setup.py install`` or ``sudo python
   setup.py develop`` or via whatever packaging system you may be using.

2) Alter your proxy-server.conf pipeline to have swauth instead of tempauth:

    Was::

        [pipeline:main]
        pipeline = catch_errors cache tempauth proxy-server

    Change To::

        [pipeline:main]
        pipeline = catch_errors cache swauth proxy-server

3) Add to your proxy-server.conf the section for the Swauth WSGI filter::

    [filter:swauth]
    use = egg:swauth#swauth
    set log_name = swauth
    super_admin_key = swauthkey

4) Restart your proxy server ``swift-init proxy reload``.

5) Initialize the Swauth backing store in Swift ``swauth-prep -K swauthkey``.

6) Add an account/user ``swauth-add-user -A http://127.0.0.1:8080/auth/ -K
   swauthkey -a test tester testing``.

7) Ensure it works ``st -A http://127.0.0.1:8080/auth/v1.0 -U test:tester -K
   testing stat -v``.

Contents
--------

.. toctree::
    :maxdepth: 2

    license
    details
    swauth
    middleware

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
