import json
from os import name


def main():

    data = '{"name": "John", "age": 30, "city": "New York"}'
    data_dick = json.loads(data)
    print(data)

    data_dick["name"] = "yheuda"
    data_dick["age"] = "22"
    data_dick["city"] = "Jerusalem"

    refjeson = json.dumps(data_dick)
    print(refjeson)


if __name__ == "__main__":
    main()
