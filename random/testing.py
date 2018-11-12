class A(object):
    def __test(self):
        print("I'm a test method in class A")

    def test(self):
        self.__test()


a = A()
a.test()
# a.__test()  # This fails with an AttributeError
a._A__test()  # Works! We can access the mangled name directly!


class B(A):
    def __test(self):
        print("I'm test method in class B")


b = B()
b.test()
b._A__test()
b._B__test()

print(A)