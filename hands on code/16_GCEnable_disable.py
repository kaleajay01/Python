import gc

class A:
    def __del__(self):
        print("cyclic remove")

gc.disable()

a = A()
c = a
b = A()

a.other = b
b.other = a

del a
del b
# del c

print("Before:", gc.collect())
