import string


def main():
    """armyCalculation("M", 20.1)
    armyCalculation("F", 20.1)
    armyCalculation("M", 22)
    armyCalculation("F", 17)

    earlyLetters("b", "c")
    earlyLetters("d", "a")
    """


# 1
def solvingQuadraticEquation(numberA, numberB, numberC):
    pass


# 2
def armyCalculation(gender, age):
    if age < 18:
        print("Before Army")
    elif age >= 18 and age <= 20 and gender == "F":
        print("Serving Currently")
    elif age >= 18 and age < 20.8 and gender == "M":
        print("Serving Currently")
    else:
        print("After Army")


# 3
def earlyLetters(laterA, laterB):
    if laterA < laterB:
        print(laterA)
    else:
        print(laterB)


# 4
def isprime(number):
    if number < 2:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True


def primeNumbers(number):
    for index in range(2, number):
        if isprime(index):
            print(index)


# 5
def Oldest():
    numberPeople = input("Enter number of people: ")
    ageOldest = 0
    nameOldest = ""
    while numberPeople > 0:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        if age > ageOldest:
            ageOldest = age
            nameOldest = name
    print(
        "The name of the most mature person is"
        + nameOldest
        + "and his age is"
        + ageOldest
    )


# 6
def LongName():
    longName = ""
    numberPeople = input("Enter number of people per intake: ")
    index = 0

    while index < numberPeople:
        name = input("Enter your name: ")
        if len(longName) < len(name):
            longName = name
        print(longName)
        index += 1


if __name__ == "__main__":
    main()
