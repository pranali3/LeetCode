from collections import Counter


def minSteps(self, s: str, t: str) -> int:
    return sum((Counter(s) - Counter(t)).values())


if __name__ == "__main__":
    s = "abad"
    t = "babe"
    print(Counter(s))
    print(Counter(t))
    print((Counter(t) - Counter(s)))
    print((Counter(s) - Counter(t)).values())
    print(sum((Counter(s) - Counter(t)).values()))
