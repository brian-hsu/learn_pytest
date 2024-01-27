class Task:
    def __init__(self, name, person):
        self.name = name
        self.person = person

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.name == other.name and self.person == other.person
        return False

    def to_dict(self):
        return {"name": self.name, "person": self.person}