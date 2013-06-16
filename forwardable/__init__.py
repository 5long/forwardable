__version__ = '0.1.0'

__all__ = ["forwardable", "def_delegator", "def_delegators"]

import sys

class NotCalledInModuleScope(Exception): pass
class NotCalledInClassScope(Exception): pass
class WrongDecoratorSyntax(Exception): pass

def def_delegator(wrapped, attr_name, _call_stack_depth=1):
    frame = sys._getframe(_call_stack_depth)

    if not looks_like_class_frame(frame):
        raise NotCalledInClassScope

    def getter(self):
        return getattr(getattr(self, wrapped), attr_name)

    scope = frame.f_locals
    scope[attr_name] = property(getter)


def def_delegators(wrapped, attrs):
    for a in attrs:
        def_delegator(wrapped, a, _call_stack_depth=2)


CLS_SCOPE_KEYS = ("__module__",)
def looks_like_class_frame(frame):
    return all(k in frame.f_locals for k in CLS_SCOPE_KEYS)

def is_module_frame(frame):
    return frame.f_globals is frame.f_locals

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
    frame = sys._getframe(1)
    inject(frame)

    def decorate(cls):
        cleanup(frame.f_locals)
        return cls

    return decorate
