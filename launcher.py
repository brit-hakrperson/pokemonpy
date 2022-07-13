import os
import codecs
import binascii
import numpy as np
import pandas as pd
from pkpy import Pokemon


def main(path: str):
    path1 = "data/test-hawlucha-g6.pk6"
    path2 = "data/test-hawlucha-bl.pk7"
    # gen6 = Pokemon(path1)
    gen7 = Pokemon("testiv.pk7")
    for item in gen7.bytemap:
        thing = gen7.bytemap[item]
        num = int(thing.split("x")[-1], 16)
        # if gen7.bytemap[item] != "0x0" or gen6.bytemap[item] != "0x0":
        # print(f"{item} :: {thing} :: {num} :: {bin(num)} :: {chr(num)}")
    
    print(gen7.trainerIDs.SID)
    # gen7.dump()


if __name__ == "__main__":
    # path = input("Enter Path >> ")
    path = "data/test-hawlucha-g7.pk7"
    main(path)
