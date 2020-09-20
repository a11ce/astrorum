import random

ROOM_TYPES = ("BRIDGE", "WEAPONS", "WORKSHOP", "SENSORS", "LAB", "COMMS")

class ShipRoom:
    def __init__(self, roomType=None):
        self.roomType = random.choice(ROOM_TYPES) if not roomType else roomType
        
    def __str__(self):
        return self.roomType.title()