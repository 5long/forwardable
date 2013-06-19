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

The ``@forwardable.forwardable()`` decorator enables you to use
``def_delegator`` in a class definition block.

.. code-block:: python

  from forwardable import forwardable

  @forwardable() # Note the () here, which is required.
  class Foo(object):
      def_delegators('bar', ('add', '__len__'))

      def __init__(self)
          self.bar = set()

  foo = Foo()
  foo.add(1) # Delegates to foo.bar.add()
  assert len(foo) == 1

Easy, heh?

In case you only need to delegate one method to a delegatee, just
use ``def_delegator``:

.. code-block:: python

  from forwardable import forwardable

  @forwardable()
  class Foo(object):
      def_delegator('bar', '__len__')

      def __init__(self)
          self.bar = set()

  assert len(Foo()) == 0

And it should work just fine.

Less Magical Usage
~~~~~~~~~~~~~~~~~~

If you hesitate to touch the ``@forwardable()`` injection magic, just
``from forwardable import def_delegator, def_delegators``, use them in
a class definition and you'll be fine.

License
-------

MIT license.

.. _forwardable: http://ruby-doc.org/stdlib-2.0/libdoc/forwardable/rdoc/Forwardable.html
