Forwardable
===========

Utility for easy object composition via delegation. Roughly ported from
Ruby's forwardable_ standard library.

Requirements
------------

Python 2.7 or 3.3 w/ standard library. Might work on other version of
Python, too.

Installation
------------

``$ pip install forwardable``

Usage
-----

Most Common Use Case
~~~~~~~~~~~~~~~~~~~~

The ``@forwardable.forwardable()`` decorator enables you to use
``def_delegator()`` and ``def_delegators()`` in a class definition block.

Use ``def_delegators()`` to define multiple attr forwarding:

.. include:: example/common_use_case.py
   :code: python

Easy, heh?

Define a Single Forwarding
~~~~~~~~~~~~~~~~~~~~~~~~~~

In case you only need to delegate one method to a delegatee, just
use ``def_delegator``:

.. include:: example/def_delegator.py
   :code: python

And it should work just fine. Actually, ``def_delegators()`` calls
``def_delegator()`` under the hood.

Plucking
~~~~~~~~

.. include:: example/plucking.py
   :code: python

Less Magical Usage
~~~~~~~~~~~~~~~~~~

The ``@forwardable()`` decorator injects ``def_delegator{,s}()`` into the
module scope temorarily, which is why you don't have to import them
explicitly. This is admittedly magical but discourages the usage
of ``import *``. And it's always nice to type less characters whenever
unnecessary.

If you hesitate to utilize this injection magic, just explicitly say
``from forwardable import def_delegator, def_delegators``, use them in
a class definition and you'll be fine.

License
-------

MIT license.

.. _forwardable: http://ruby-doc.org/stdlib-2.0/libdoc/forwardable/rdoc/Forwardable.html
