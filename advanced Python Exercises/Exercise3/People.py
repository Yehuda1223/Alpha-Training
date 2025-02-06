class Person:
    def __init__(self, persons):
        self.persons = persons

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.persons) == 0:
            raise StopIteration
        return self.persons.pop(0)

    def add_person(self, person):
        self.persons.append(person)
