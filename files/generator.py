class Demo:
    def __init__(self):
        self.data = [0, 1, 1, 2, 3, 5, 8]
        self._gen = self.make_generator()

    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self._gen)


    def make_generator(self):
        for x in self.data:
            yield x

d = Demo()
itr = iter(d)
print (next(d))
for x in d:
    print (x)
