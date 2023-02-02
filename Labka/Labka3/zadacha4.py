# Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.
f = int(input())
g = int(input())


class MyNumbers:
    def __iter__(self):
        self.a = g

        return self

    def __next__(self):
        if self.a >= f:
            x = self.a
            self.a -= 2  # реалицазия условии for здесь работает

            return x

        else:
            raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))