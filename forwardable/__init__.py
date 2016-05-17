"""
Easy delegation definition. A quick example:

    from forwardable import forwardable

    @forwardable() # Note the () here, which is required.
    class Foo(object):
        def_delegators('bar', 'add, __len__')

        def __init__(self)
            self.bar = set()

    foo = Foo()
    foo.add(1) # Delegates to foo.bar.add()
    assert len(foo) == 1
"""

__version__ = '0.4.1'

__all__ = ["forwardable", "def_delegator", "def_delegators"]

try:
    basestring
except NameError:
    basestring = (str, bytes)

import sys
from operator import attrgetter

class NotCalledInModuleScope(Exception): pass
class NotCalledInClassScope(Exception): pass
class WrongDecoratorSyntax(Exception): pass

def def_delegator(wrapped, attr_name, _call_stack_depth=1):
    """
    Define a property ``attr_name`` in the current class scope which
    forwards accessing of ``self.<attr_name>`` to property
    ``self.<wrapped>.<attr_name>``.

    Must be called in a class scope.
    """
    frame = sys._getframe(_call_stack_depth)

    if not looks_like_class_frame(frame):
        raise NotCalledInClassScope

    get_wrapped_obj = attrgetter(wrapped)

    def getter(self):
        return getattr(get_wrapped_obj(self), attr_name)

    def setter(self, value):
        return setattr(get_wrapped_obj(self), attr_name, value)

    def deleter(self):
        return delattr(get_wrapped_obj(self), attr_name)

    scope = frame.f_locals
    scope[attr_name] = property(getter, setter, deleter)


def def_delegators(wrapped, attrs):
    """
    Define multiple delegations for a single delegatee. Roughly equivalent
    to def_delegator() in a for-loop.

    The ``attrs`` argument can be an iterable of attribute names, or
    a comma-and-spaces separated string of attribute names. The following
    form works identically:

    def_delegators(wrapped, ('foo', 'bar')) # Tuple of attribute names
    def_delegators(wrapped, 'foo bar')      # Separated by space
    def_delegators(wrapped, 'foo, bar')     # With optional comma

    Must be called in a class scope.
    """
    attrs = split_attrs(attrs) if isinstance(attrs, basestring) else attrs
    for a in attrs:
        def_delegator(wrapped, a, _call_stack_depth=2)


CLS_SCOPE_KEYS = ("__module__",)
def looks_like_class_frame(frame):
    return all(k in frame.f_locals for k in CLS_SCOPE_KEYS)

def is_module_frame(frame):
    return frame.f_globals is frame.f_locals

def split_attrs(attrs):
    return attrs.replace(',', ' ').split()

def inject(frame):
    if not is_module_frame(frame):
        raise NotCalledInModuleScope()
    frame.f_locals.update(
            def_delegator=def_delegator,
            def_delegators=def_delegators)


def cleanup(scope):
    scope.pop("def_delegator")
    scope.pop("def_delegators")


def forwardable():
    """
    A class decorator which makes def_delegator() and def_delegators()
    available in the class scope.

    This decorator must be used in the form of `@forwardable()`, instead of
    `@forwardable`. And it must be called in a module scope (which should be
    the case for most common class definitions).
    """
    frame = sys._getframe(1)
    inject(frame)

    def decorate(cls):
        cleanup(frame.f_locals)
        return cls

    return decorate
