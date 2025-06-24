from enum import Enum, auto


class State(Enum):
    LOCKED = auto()
    UNLOCKED = auto()
    FAILED = auto()


if __name__ == "__main__":
    state = State.LOCKED
    code = "1234"
    while True:
        if state == State.LOCKED:
            entry = input("enter the key:\n")
            if code == entry:
                state = State.UNLOCKED
            else:
                state = State.FAILED

        elif state == State.UNLOCKED:
            print("\nUNLOCKED")
            break
        elif state == State.FAILED:
            print("\nFAILED")
            state = State.LOCKED
