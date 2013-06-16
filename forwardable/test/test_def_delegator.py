from unittest import TestCase

from forwardable import (def_delegator, def_delegators,
        NotCalledInClassScope)

class TestForwardable(TestCase):
    def test_def_delegator(self):
        class Foo(object):
            def_delegator("dct", "keys")
            dct = {'key': 42}

        foo = Foo()

        self.assertTrue(hasattr(foo, "keys"))
        self.assertEqual(foo.keys(), ['key'])


    def test_def_delegators(self):
        class Foo(object):
            def_delegators("dct", ["keys", "values"])
            dct = {'key': 42}

        foo = Foo()

        self.assertEqual(foo.keys(), ['key'])
        self.assertEqual(foo.values(), [42])

    def test_called_in_non_class_scope(self):
        with self.assertRaises(NotCalledInClassScope):
            def_delegator("what", "ever")


    def test_delegating_special_method(self):
        class Foo(object):
            def_delegator("s", "__len__")
            def __init__(self):
                self.s = set()

        self.assertEqual(len(Foo()), 0)
