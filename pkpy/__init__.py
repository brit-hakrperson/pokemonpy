from pkpy.structs import *
from pkpy.converter import *


class Pokemon():
    def __init__(self, path):
        self.raw = open(path, "rb")
        self.bytemap = {}
        self.__data = []

        self.__scrapeData()

        self.encryptionKey = self._slice("0x00", "0x03")
        self.checksum = self._slice("0x06", "0x07")

        self.dexID = self._slice("0x08", "0x09")
        self.heldItem = self._slice("0x0a", "0x0b")
        self.trainer = PKIDs(str(hexToInt(self._slice("0x0c", "0x0f"))))
        self.exp = hexToInt(self._slice("0x10", "0x13"))
        self.ability = self._getOffset("0x14")
        self.abilityNo = self._getOffset("0x15")
        self.hitsRemaining = None
        self.PID = self._slice("0x18", "0x1b")
        self.nature = self._getOffset("0x1c")
        self.variations = PKVariations(self._getOffset("0x1d"))
        self.effortVal = PKEffort(self._slice("0x1e", "0x23", 1))
        self.contestStat = PKContest(self._slice("0x24", "0x29", 1))
        self.markings = self._getOffset("0x2a")
        self.pokerus = self._getOffset("0x2b")
        self.superTrainGMF = self._slice("0x2c", "0x2f")
        self.ribbons = self._slice("0x30", "0x35")
        self.contestMemRC = hexToInt(self._getOffset("0x38"))
        self.battleMemRC = hexToInt(self._getOffset("0x39"))
        self.superTrainFlags = self._getOffset("0x3a")
        self.nickname = self._formatStr(self._slice("0x40", "0x57", 1))
        self.superTrainFlag = self._getOffset("0x72")

        self.moves = PKMoves([
            self._slice("0x5a", "0x5b"),
            self._getOffset("0x62"),
            self._slice("0x5c", "0x5d"),
            self._getOffset("0x63"),
            self._slice("0x5e", "0x5f"),
            self._getOffset("0x64"),
            self._slice("0x60", "0x61"),
            self._getOffset("0x65"),
            self._slice("0x66", "0x69")
        ])

        self.relearn = PKRelearn([
            self._slice("0x6a", "0x6b"),
            self._slice("0x6c", "0x6d"),
            self._slice("0x6e", "0x6f"),
            self._slice("0x70", "0x71")
        ])

        self.coreInfo = PKCore(
            self._slice("0x74", "0x77")
        )
        '''
        self.currentTrainer = PKCT([
            self._formatStr(self._slice("0x78", "0x8f", 1)),
            self._getOffset("0x92"),
            self._getOffset("0x93"),
            self._slice("0x94", "0x95"),
            self._slice("0x96", "0x97"),
            self._slice("0x98", "0x99"),
            self._slice("0x9a", "0x9b"),
            self._slice("0x9c", "0x9d"),

        ])'''

        self.raw.close()

    def __scrapeData(self):
        count = 0
        for line in self.raw.readlines():
            for byte in line:
                self.bytemap[hex(count)] = hex(byte)
                self.__data.append(("00" + hex(byte).split("x")[-1])[-2:])
                count += 1

    def _slice(self, srt, end, order=-1):
        stuff = []
        for val in self.__data[hexToInt(srt):hexToInt(end)+1][::order]:
            stuff.append(("00" + val)[-2:])
        return "".join(stuff)

    def _formatStr(self, data: list):
        # select every 2i+1 item
        # switch-merge with every 2i+2 item
        char = []
        for j in range(len(data)//2):
            i = 2 * j + 1
            char.append(hexToChar(data[i-1] + data[i]))
        return "".join(char)

    def _getOffset(self, hexNum):
        return hexToInt(self.bytemap[hexNum])

    def dump(self):
        with open("dump.txt", "w", encoding="latin-1") as dump:
            for offset in self.bytemap:
                index = str(("  " + offset)[-4:])
                data = str(("  " + self.bytemap[offset])[-4:])
                num = str(("00" + str(hexToInt(data)))[-3:])
                char = str(chr(int(num)))
                line = f"{index} : {data} : {num} : {char}"
                dump.write(line + "\n")

    def __del__(self):
        pass
