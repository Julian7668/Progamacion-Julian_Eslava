import random


def flip_coin() -> str:
    return random.choice(["Cara", "Cruz"])


if __name__ == "__main__":
    print(flip_coin())
