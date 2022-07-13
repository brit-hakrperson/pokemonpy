import os, codecs
import binascii
import numpy as np
import pandas as pd
from offsetref import offsetRef

class Pokemon():
    def __init__(self, path):
        self.raw = open(path, "rb")
        self.bytemap = {}
        self.__data = []
        
        self.__scrapeData()

        self.encryptionKey  = self._slice("0x00", "0x03")
        self.checksum       = self._slice("0x06", "0x07")
        self.dexID          = self._slice("0x", end)

    def __scrapeData(self):
        count = 0
        for line in self.raw.readlines():
            for byte in line:
                self.bytemap[hex(count)] = hex(byte)
                self.__data.append(hex(byte).split("x")[-1])
                count += 1
    
    def _slice(self, srt, end):
        return "".join(self.__data[self.hexToInt(srt):self.hexToInt(end)+1][::-1])

    def hexToInt(self, hexNum):
        return int(hexNum.split("x")[-1], 16)

    def __del__(self):
        self.raw.close()


def main(path: str):
    path1 = "test-hawlucha-g6.pk6"
    path2 = "test-hawlucha-bl.pk7"
    gen6 = Pokemon(path1)
    gen7 = Pokemon(path2)
    '''
    for item in gen7.bytemap:
        thing = gen7.bytemap[item]
        num = int(thing.split("x")[-1], 16)
        # if gen7.bytemap[item] != "0x0" or gen6.bytemap[item] != "0x0":
        print(f"{item} :: {thing} :: {num} :: {bin(num)} :: {chr(num)}")
    '''
    
    print(gen7.encryptionKey)
    print(gen7.checksum)



if __name__ == "__main__":
    # path = input("Enter Path >> ")
    path = "test-hawlucha-g7.pk7"
    main(path)
    
