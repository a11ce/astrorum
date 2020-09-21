from game import randomGen as gen
from game import PlayerIO as IO

from objects import People
from objects import Rooms
from objects import Cargo


class Ship:
    def __init__(self,
                 name=None,
                 cargo=[],
                 crew=None,
                 cargoCap=100,
                 crewCap=6,
                 roomCap=7):
        self.name = name
        self.cargo = cargo
        self.cargoCap = cargoCap
        self.crew = crew
        self.crewCap = crewCap
        self.roomCap = roomCap
        self.rooms = [Rooms.ShipRoom() for _ in range(roomCap)]

    def __str__(self):
        s = ""
        s += "Name is {}\n".format(self.name)
        s += "Cargo is:\n"
        for cargoObj in self.cargo:
            s += str(cargoObj) + "\n"
        s += "Crew is:\n"
        for crewM in self.crew:
            s += str(crewM) + "\n"
        s += "Rooms are:\n"
        for room in self.rooms:
            s += str(room) + "\n"
        s += "CargoCap is {}\n".format(self.cargoCap)
        s += "CrewCap is {}\n".format(self.crewCap)
        return s


class AIShip(Ship):
    def __init__(self,
                 name=None,
                 cargo=None,
                 crew=None,
                 cargoCap=100,
                 crewCap=6,
                 roomCap=7):
        super(AIShip, self).__init__()
        self.name, self.lang = (name, None) if name else gen.shipName()
        self.cargo = cargo if cargo else [Cargo.Cargo("Artifact", weight=100)]
        self.cargoCap = crewCap * 20
        self.crew = [
            People.Crew(name=gen.personName(self.lang)) for _ in range(crewCap)
        ]
        self.crewCap = crewCap


class PlayerShip(Ship):
    def __init__(self, **kwargs):
        super(PlayerShip, self).__init__(**kwargs)
        #self.crewCap = 6
        self.name = IO.askText("Name your new ship:")
        IO.titlePrint()
        self.crew = IO.selectFrom([
            People.Crew(name=gen.personName()[0]) for _ in range(self.crewCap)
        ], (self.crewCap //2))
        self.rooms = [Rooms.ShipRoom(roomType=x) for x in IO.selectFrom(Rooms.ROOM_TYPES, self.roomCap, displayFunc = lambda x : x.title())]