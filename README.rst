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

.. code-block:: python

    from forwardable import forwardable

    @forwardable() # Note the () here, which is required.
    class Foo(object):
        def_delegators('bar', 'add, __len__')

        def __init__(self):
            self.bar = set()

    foo = Foo()
    foo.add(1) # Delegates to foo.bar.add()
    assert len(foo) == 1 # Magic methods works, too

Easy, heh?

Define a Single Forwarding
~~~~~~~~~~~~~~~~~~~~~~~~~~

In case you only need to delegate one method to a delegatee, just
use ``def_delegator``:

.. code-block:: python

    from forwardable import forwardable

    @forwardable()
    class Foo(object):
        def_delegator('bar', '__len__')

        def __init__(self):
            self.bar = set()

    assert len(Foo()) == 0

And it should work just fine. Actually, ``def_delegators()`` calls
``def_delegator()`` under the hood.

Plucking
~~~~~~~~

.. code-block:: python

    from forwardable import forwardable

    @forwardable()
    class MyDict(object):
        def_delegator('dct.get', '__call__')
        def __init__(self):
            self.dct = {'foo', 42}

    d = MyDict()
    # Equivlant to d.dct.get('foo')
    assert d('foo') == 42

Less Magical Usage
~~~~~~~~~~~~~~~~~~

The ``@forwardable()`` decorator injects ``def_delegator{,s}`` into the
module scope temorarily, which is why you don't have to import them
explicitly. This is admittedly magical but discourages the usage
of ``import *``. And it's always nice to type less characters whenever
unnecessary.

If you hesitate to utilize this injection magic, just explicitly say
``from forwardable import def_delegator, def_delegators``, use them in
a class definition and you'll be fine.

Links
-----

* Source Repository: https://github.com/5long/forwardable
* Feedback: https://github.com/5long/forwardable/issues

License
-------

MIT license.

.. _forwardable: http://ruby-doc.org/stdlib-2.0/libdoc/forwardable/rdoc/Forwardable.html
