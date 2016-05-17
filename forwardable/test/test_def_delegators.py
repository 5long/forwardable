from unittest import TestCase

from forwardable import def_delegators

class TestDefDelegators(TestCase):
    def test_def_delegators(self):
        class Foo(object):
            def_delegators("dct", ["keys", "values"])
            dct = {'key': 42}

        foo = Foo()

        self.assertEqual(list(foo.keys()), ['key'])
        self.assertEqual(list(foo.values()), [42])

    def test_attr_splitting(self):
        class Foo(object):
            def_delegators("dct", "keys, values")
            dct = {'key': 42}

        foo = Foo()

        self.assertEqual(list(foo.keys()), ['key'])
        self.assertEqual(list(foo.values()), [42])
