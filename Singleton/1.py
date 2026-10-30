class Singleton:
    _instance = None

    def __new__(cls,balance):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


a = Singleton(200)
b = Singleton(300)
print((a))
print(a is b)  # True