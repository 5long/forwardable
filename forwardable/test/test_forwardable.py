from unittest import TestCase

from forwardable import (forwardable, NotCalledInModuleScope,
        WrongDecoratorSyntax)

assert "def_delegator" not in locals()

@forwardable()
class Foo(object):
    assert "def_delegator" not in locals()
    def_delegator('dct', 'keys')
    def_delegators('dct', ['values', 'items'])
    dct = {'key': 42}


assert "def_delegator" not in locals()

class TestForwardable(TestCase):
    def test_inject_def_delegator(self):
        foo = Foo()

        self.assertEqual(list(foo.keys()), ['key'])
        self.assertEqual(list(foo.values()), [42])
        self.assertEqual(list(foo.items()), [('key', 42)])

        self.assertFalse(hasattr(foo, "get")) 

    def test_in_non_module_scope(self):
        with self.assertRaises(NotCalledInModuleScope):
            @forwardable()
            class Foo(object):
                pass

    def test_wrong_decorator_syntax(self):
        with self.assertRaises(Exception):
            @forwardable
            class Foo(object):
                pass
