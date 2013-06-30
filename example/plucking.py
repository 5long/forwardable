from forwardable import forwardable

@forwardable
class MyDict(object):
    def_delegator('dct.get', '__call__')
    def __init__(self):
        self.dct = {'foo', 42}

d = MyDict()
# Equivlant to d.dct.get('foo')
assert d('foo') == 42
