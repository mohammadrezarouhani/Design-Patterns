# we use singletone when we want to instanciate once from an object like database connection
# any extra database connection is just waste of memory and resources


class Database:
    instance = None

    def __init__(
        self,
    ):  # the problem within this aproach is, every time initialyzer will be called
        print("loading database!")

    def __new__(cls, *args, **kwargs):  # we can acive it like this
        if not cls.instance:
            cls.instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls.instance




if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 is d2)
