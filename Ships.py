import randomGen as gen
import People

class Ship:
    def __init__(self, name=None, cargo=[], crew=None, cargoCap=100, crewCap=6):
        self.name = name
        self.cargo = cargo
        self.cargoCap = cargoCap
        self.crew = crew
        self.crewCap = crewCap

    def __str__(self):
        s = ""
        s += "Name is {}\n".format(self.name)
        s += "Cargo is {}\n".format(self.cargo)
        s += "Crew is:\n"
        for crewM in self.crew:
            s += str(crewM) + "\n"
        s += "CargoCap is {}\n".format(self.cargoCap)
        s += "CrewCap is {}\n".format(self.crewCap)
        return s

class AIShip(Ship):
    def __init__(self, name=None, cargo=[], crew=None, cargoCap=100, crewCap=6):
        self.name = name if name else gen.shipName()
        self.cargo = cargo
        self.cargoCap = crewCap * 20
        self.crew = [People.Crew(name = gen.personName()) for _ in range(crewCap)]
        self.crewCap = crewCap