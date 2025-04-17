class SingleTone(type):
    intances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls.intances:
            cls.intances[cls] = super(SingleTone, cls).__call__(*args, **kwds)
        return cls.intances[cls]


class Database(metaclass=SingleTone):
    def __init__(self):
        print("loading database!")


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    d3 = Database()
    print(d1 == d2)
