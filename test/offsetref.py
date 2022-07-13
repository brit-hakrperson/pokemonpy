def offsetRef(offset: hex):
    ref = {'0x0': 'Encryption KEy', '0x1': 'Encryption Key', '0x2': 'Encryption Key', '0x3': 'Encryption KEy', '0x4': 'Placeholder', '0x5': 'Placeholder', '0x6': 'Checksum', '0x7': 'Checksum', '0x8': 'NPID', '0x9': 'NPID', '0xa': 'Held Item', '0xb': 'Held Item', '0xc': 'OT ID', '0xd': 'OT ID', '0xe': 'OT Secret', '0xf': 'OT Secret', '0x10': 'EXP', '0x11': 'EXP ', '0x12': 'EXP', '0x13': 'EXP', '0x14': 'Ability', '0x15': 'Ability No.', '0x16': 'HP Remaining', '0x17': 'HP Remaining', '0x18': 'PID', '0x19': 'PID', '0x1a': 'PID', '0x1b': 'PID', '0x1c': 'Nature', '0x1d': 'Variations', '0x1e': 'EV HP', '0x1f': 'EV ATK', '0x20': 'EV DEF', '0x21': 'EV SPD', '0x22': 'EV S-ATK', '0x23': 'EV S-DEF', '0x24': 'CS Cool', '0x25': 'CS Beauty', '0x26': 'CS Cute', '0x27': 'CS Smart', '0x28': 'CS Tough', '0x29': 'CS Sheen', '0x2a': 'Markings', '0x2b': 'Pokerus', '0x2c': 'Secret ST GMF', '0x2d': 'Secret ST GMF', '0x2e': 'Secret ST GMF', '0x2f': 'Secret ST GMF', '0x30': 'Ribbons', '0x31': 'Ribbons', '0x32': 'Ribbons', '0x33': 'Ribbons', '0x34': 'Ribbons', '0x35': 'Ribbons', '0x36': 'n/a', '0x37': 'n/a', '0x38': 'Count Contest MR', '0x39': 'Count Battle MR', '0x3a': 'Distrobution ST Flags', '0x3b': 'n/a', '0x3c': 'n/a', '0x3d': 'n/a', '0x3e': 'n/a', '0x3f': 'n/a', '0x40': 'Nickname', '0x41': 'Nickname', '0x42': 'Nickname', '0x43': 'Nickname', '0x44': 'Nickname', '0x45': 'Nickname', '0x46': 'Nickname', '0x47': 'Nickname', '0x48': 'Nickname', '0x49': 'Nickname', '0x4a': 'Nickname', '0x4b': 'Nickname', '0x4c': 'Nickname', '0x4d': 'Nickname', '0x4e': 'Nickname', '0x4f': 'Nickname', '0x50': 'Nickname', '0x51': 'Nickname', '0x52': 'Nickname', '0x53': '\x16', '0x54': 'Nickname', '0x55': 'Nickname', '0x56': 'Nickname', '0x57': 'Nickname', '0x58': 'Null Terminator', '0x59': 'Null Terminator', '0x5a': 'Move 1 ID', '0x5b': 'Move 1 ID', '0x5c': 'Move 2 ID', '0x5d': 'Move 2 ID', '0x5e': 'Move 3 ID', '0x5f': 'Move 3 ID', '0x60': 'Move 4 ID', '0x61': 'Move 4 ID', '0x62': 'Move 1 Current PP', '0x63': 'Move 1 Current PP', '0x64': 'Move 3 Current PP', '0x65': 'Move 4 Current PP', '0x66': 'Move PP Ups', '0x67': 'Move PP Ups', '0x68': 'Move PP Ups', '0x69': 'Move PP Ups', '0x6a': 'RLM 1 ID', '0x6b': 'RLM 1 ID', '0x6c': 'RLM 2 ID', '0x6d': 'RLM 2 ID', '0x6e': 'RLM 3 ID', '0x6f': 'RLM 3 ID', '0x70': 'RLM 4 ID', '0x71': 'RLM 4 ID', '0x72': 'Secret Super Train Flag', '0x73': 'n/a', '0x74': 'IV Misc', '0x75': 'IV Misc', '0x76': 'IV Misc', '0x77': 'IV Misc', '0x78': 'Latest Not-OT', '0x79': 'Latest Not-OT', '0x7a': 'Latest Not-OT', '0x7b': 'Latest Not-OT', '0x7c': 'Latest Not-OT', '0x7d': 'Latest Not-OT', '0x7e': 'Latest Not-OT', '0x7f': 'Latest Not-OT', '0x80': 'Latest Not-OT', '0x81': 'Latest Not-OT',
           '0x82': 'Latest Not-OT', '0x83': 'Latest Not-OT', '0x84': 'Latest Not-OT', '0x85': 'Latest Not-OT', '0x86': 'Latest Not-OT', '0x87': 'Latest Not-OT', '0x88': 'Latest Not-OT', '0x89': 'Latest Not-OT', '0x8a': 'Latest Not-OT', '0x8b': '\x16', '0x8c': 'Latest Not-OT', '0x8d': 'Latest Not-OT', '0x8e': 'Latest Not-OT', '0x8f': 'Latest Not-OT', '0x90': 'Null Terminator', '0x91': 'Null Terminator', '0x92': 'Not-OT Gender', '0x93': 'Current Handler', '0x94': 'GeoLoc 1', '0x95': 'GeoLoc 1', '0x96': 'GeoLoc 2', '0x97': 'GeoLoc 2', '0x98': 'GeoLoc 2', '0x99': 'GeoLoc 3', '0x9a': '', '0x9b': 'GeoLoc 4', '0x9c': 'GeoLoc 5', '0x9d': 'GeoLoc 5', '0x9e': 'n/a', '0x9f': 'n/a', '0xa0': 'n/a', '0xa1': 'n/a', '0xa2': 'NotOT Friendship', '0xa3': 'NotOT Affection', '0xa4': 'NotOT Memory Line', '0xa5': 'NotOT Memory Feeling', '0xa6': 'n/a', '0xa7': 'NotOT Memory Text Var', '0xa8': 'NotOT MEmory Text Var', '0xa9': 'n/a', '0xaa': 'n/a', '0xab': 'n/a', '0xac': 'n/a', '0xad': 'n/a', '0xae': 'Fullness', '0xaf': 'Enjoyment', '0xb0': 'OT Name', '0xb1': 'OT Name', '0xb2': 'OT Name', '0xb3': 'OT Name', '0xb4': 'OT Name', '0xb5': 'OT Name', '0xb6': 'OT Name', '0xb7': 'OT Name', '0xb8': 'OT Name', '0xb9': 'OT Name', '0xba': 'OT Name', '0xbb': 'OT Name', '0xbc': 'OT Name', '0xbd': 'OT Name', '0xbe': 'OT Name', '0xbf': 'OT Name', '0xc0': 'OT Name', '0xc1': 'OT Name', '0xc2': 'OT Name', '0xc3': 'OT Name', '0xc4': 'OT Name', '0xc5': 'OT Name', '0xc6': 'OT Name', '0xc7': 'OT Name', '0xc8': 'Null Terminator', '0xc9': 'Null Terminator', '0xca': 'OT FRiendship', '0xcb': 'OT Affection', '0xcc': 'OT Mem Intensity', '0xcd': 'OT Mem Line', '0xce': 'OT Mem TextVar', '0xcf': 'OT Mem TextVar', '0xd0': 'OT MEm Feeling', '0xd1': 'Date Egg rEcieved ', '0xd2': 'Date Egg rEcieved', '0xd3': 'Date Egg recieved', '0xd4': 'Date <et', '0xd5': 'Date MEt', '0xd6': 'Date Met', '0xd7': '?????', '0xd8': 'Egg Location', '0xd9': 'Egg Location', '0xda': 'MEtAt Location', '0xdb': 'MetAT Location', '0xdc': 'Pokeball', '0xdd': 'Encounter+OT Gender', '0xde': 'Encounter Type', '0xdf': 'OT Game ID', '0xe0': 'Country ID', '0xe1': 'REgion ID', '0xe2': '3DS Region ID', '0xe3': 'OT Lang ID', '0xe4': 'n/a', '0xe5': 'n/a', '0xe6': 'n/a', '0xe7': 'n/a', '0xe8': 'Condition', '0xe9': '?????', '0xea': '?????', '0xeb': '?????', '0xec': 'Level', '0xed': '?????', '0xee': '?????', '0xef': '?????', '0xf0': 'Current HP', '0xf1': 'Current HP', '0xf2': 'Max HP', '0xf3': 'MAx HP', '0xf4': 'ATK', '0xf5': 'ATK', '0xf6': 'DEF', '0xf7': 'DEF', '0xf8': 'SPD', '0xf9': 'SPD', '0xfa': 'S ATK', '0xfb': 'S ATK', '0xfc': 'S DEF', '0xfd': 'S DEF', '0xfe': '?????', '0xff': '?????', '0x100': 'JPN', '0x101': 'ENG Lang', '0x102': 'FRN Lang', '0x103': 'ITL LAng'}
    return ref[offset]

def hexToInt(self, hexNum):
    return int(hexNum.split("x")[-1], 16)
