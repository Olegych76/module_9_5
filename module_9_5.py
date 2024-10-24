class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        if step == 0:
            raise StepValueError
        elif step > 0 and stop < start or step < 0 and stop > start:
            raise StepValueError
        else:
            self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step > 0 and self.pointer > self.stop or self.step < 0 and self.pointer < self.stop:
            raise StopIteration
        else:
            value = self.pointer
            self.pointer += self.step
            return value


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')

except StepValueError:
    print('Шаг не может быть равен нулю')

iter2 = Iterator(-5, 1)
for i in iter2:
    print(i, end=' ')
print()

iter3 = Iterator(6, 15, 2)
for i in iter3:
    print(i, end=' ')
print()

iter4 = Iterator(5, 1, -1)
for i in iter4:
    print(i, end=' ')
print()

try:
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=' ')
    print()

except StepValueError:
    print('В этом (>) направлении нельзя')

try:
    iter6 = Iterator(1, 5, -1)
    for i in iter6:
        print(i, end=' ')
    print()

except StepValueError:
    print('В этом (<) направлении нельзя')
