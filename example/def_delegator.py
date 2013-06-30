from forwardable import forwardable

@forwardable()
class Foo(object):
    def_delegator('bar', '__len__')

    def __init__(self):
        self.bar = set()

assert len(Foo()) == 0
