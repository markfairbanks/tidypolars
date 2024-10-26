class pipe(object):
    __name__ = "pipe"

    def __init__(self, function):
        self.function = function
        self.__doc__ = function.__doc__

        self.chained_pipes = []

    def __rshift__(self, other):
        assert isinstance(other, pipe)
        self.chained_pipes.append(other)
        return self

    def __rrshift__(self, other):
        result = self.function(other)

        for p in self.chained_pipes:
            result = p.__rrshift__(result)
        return result

    def __call__(self, *args, **kwargs):
        return pipe(lambda x: self.function(x, *args, **kwargs))

def dfpipe(f):
    return pipe(f)