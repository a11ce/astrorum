import random

CREW_TYPES = ('PILOT', 'GUNNER', 'ENGINEER', 'SCOUT', 'SCIENTIST', 'TRADER')


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Crew(Person):
    def __init__(self, name):
        super(Crew, self).__init__(name)
        self.crewType = random.choice(CREW_TYPES)

    def __str__(self):
        return self.name + ", " + str(self.crewType).title()
