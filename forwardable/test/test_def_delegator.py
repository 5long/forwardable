from unittest import TestCase

from forwardable import (def_delegator, def_delegators,
        NotCalledInClassScope)

class Object(object):
    pass


class TestForwardable(TestCase):
    def test_def_delegator(self):
        class Foo(object):
            def_delegator("dct", "keys")
            dct = {'key': 42}

        foo = Foo()

        self.assertTrue(hasattr(foo, "keys"))
        self.assertEqual(list(foo.keys()), ['key'])


    def test_called_in_non_class_scope(self):
        with self.assertRaises(NotCalledInClassScope):
            def_delegator("what", "ever")


    def test_delegating_special_method(self):
        class Foo(object):
            def_delegator("s", "__len__")
            def __init__(self):
                self.s = set()

        self.assertEqual(len(Foo()), 0)


    def test_property_deleting(self):
        class Foo(object):
            def_delegator("bar", "baz")

        foo = Foo()
        foo.bar = Object()
        foo.bar.baz = 42

        del foo.baz
        self.assertFalse(hasattr(foo, 'baz'))


    def test_hasattr(self):
        class Foo(object):
            def_delegator("bar", "baz")

        foo = Foo()
        foo.bar = Object()

        self.assertFalse(hasattr(foo, 'baz'))

        foo.bar.baz = 42
        self.assertTrue(hasattr(foo, 'baz'))


    def test_setattr(self):
        class Foo(object):
            def_delegator("bar", "baz")

        foo = Foo()
        foo.bar = Object()
        foo.baz = 42

        self.assertTrue(foo.bar.baz, 42)


    def test_attr_plucking(self):
        class Foo(object):
            def_delegator("bar.baz", "qoox")

        foo = Foo()
        foo.bar = Object()
        foo.bar.baz = Object()
        foo.bar.baz.qoox = 42

        self.assertEqual(foo.qoox, 42)
