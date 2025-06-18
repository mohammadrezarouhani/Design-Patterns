# method 1 for handling singletone


def singleton(class_):
    instances = {}
    print("passed")

    def get_instances(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instances


@singleton
class Database:
    def __init__(self):
        print("loading database!")


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    d3 = Database()
    print(d1 == d2)