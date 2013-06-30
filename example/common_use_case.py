from forwardable import forwardable

@forwardable() # Note the () here, which is required.
class Foo(object):
    def_delegators('bar', ('add', '__len__'))

    def __init__(self):
        self.bar = set()

foo = Foo()
foo.add(1) # Delegates to foo.bar.add()
assert len(foo) == 1 # Magic methods works, too
