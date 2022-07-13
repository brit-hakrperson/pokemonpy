from pkpy.converter import *

class PKIDs():
    def __init__(self, data: str):
        self.raw = data
        self.SID = self.raw[0:4]
        self.TID = self.raw[4:]

class PKVariations():
    def __init__(self, data):
        self.raw = ("00000000" + hexToBin(data))[-8:]
        self.fatefulEnctr = self.raw[0]
        self.female = self.raw[1]
        self.genderless = self.raw[2]
        self.variation = self.raw[3:]


class PKEffort():
    def __init__(self, data: list):
        self.raw = data
        self.hitPoints = hexToInt(self.raw[0:2])
        self.attack = hexToInt(self.raw[2:4])
        self.defence = hexToInt(self.raw[4:6])
        self.speed = hexToInt(self.raw[6:8])
        self.specialAtk = hexToInt(self.raw[8:10])
        self.specialDef = hexToInt(self.raw[10:12])


class PKContest():
    def __init__(self, data: list):
        self.raw = data
        self.cool = hexToInt(self.raw[0:2])
        self.beauty = hexToInt(self.raw[2:4])
        self.cute = hexToInt(self.raw[4:6])
        self.smart = hexToInt(self.raw[6:8])
        self.tough = hexToInt(self.raw[8:10])
        self.sheen = hexToInt(self.raw[10:12])
        
class PKMove():
    def __init__(self, moveID, movePP):
        self.moveID = hexToInt(moveID)
        self.movePP = hexToInt(movePP)

class PKMoves():
    def __init__(self, data: list):
        self.move_1 = PKMove(data[0], data[1])
        self.move_2 = PKMove(data[2], data[3])
        self.move_3 = PKMove(data[4], data[5])
        self.move_4 = PKMove(data[6], data[7])
        self.ppups = data[8]


class PKRelearn():
    def __init__(self, data: list):
        self.move_1 = data[0]
        self.move_2 = data[1]
        self.move_2 = data[2]
        self.move_2 = data[3]

class PKCore():
    def __init__(self, data: list):
        self.data = []
        for item in data:
            self.data.append(("0000" + hexToBin(item))[-4:])
        self.raw = "".join(self.data)
        print(self.raw)
        self.nickname = binToInt(self.raw[0])
        self.egg = binToInt(self.raw[1])
        self.speed = binToInt(self.raw[2:7])
        self.spAtk = binToInt(self.raw[7:12])
        self.spDef = binToInt(self.raw[12:17])
        self.defence = binToInt(self.raw[17:22])
        self.attack = binToInt(self.raw[22:27])
        self.hitPoints = binToInt(self.raw[27:32])

    


