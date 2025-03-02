import time


def main():
    printHello()


def timeTaken(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start}")
        return result

    return wrapper


@timeTaken
def printHello():
    print("Hello")


if __name__ == "__main__":
    main()
