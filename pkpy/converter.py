def hexToInt(hexNum: str):
    try:
        return int(str(hexNum).split("x")[-1], 16)
    except:
        return int(str(hexNum), 16)


def hexToBin(hexNum):
    return bin(hexToInt(hexNum)).split("b")[-1]

def hexToChar(hexNum: str):
    return str(chr(hexToInt(hexNum)))

def binToInt(binNum: str):
    return str(int(binNum, 2))