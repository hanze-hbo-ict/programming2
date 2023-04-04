class Demo:
    def __init__(self):
        self.data = [0, 1, 1, 2, 3, 5, 8]

    def __iter__(self):
        for x in self.data:
            yield x
    
d = Demo()
for x in d:
    print (x)
