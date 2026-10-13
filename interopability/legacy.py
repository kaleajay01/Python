import ctypes

lib = ctypes.CDLL("./legacy.dll")

lib.increment.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.increment.restype = None

value = ctypes.c_int(10)

lib.increment(ctypes.byref(value))

print(value.value)