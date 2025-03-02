from sympy import Eq
from point import Point


def main():
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    print((p1 == p2))
    print(p1, p2)
    print(p1 + p2)


if __name__ == "__main__":
    main()
