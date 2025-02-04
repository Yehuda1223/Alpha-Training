import person


def main():
    """try:
        printNumbers(1)
    except TypeError:
        print("invalid input")
    finally:
        print("running Finished.")
    print(powerList(5))
    print(powerList(10))
    """


# 2
def printNumbers(num1, num2):
    print("num1:", num1, "num2:", num2)


#:List Comprehension
# 3
def powerList(num):
    return [x**2 for x in range(num)]


if __name__ == "__main__":
    main()
