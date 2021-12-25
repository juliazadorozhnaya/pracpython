import struct
import sys

data = sys.stdin.buffer.read()

try:
    RIFF = struct.unpack_from("4s", data, 0)[0]
    SIZE = struct.unpack_from("i", data, 4)[0]
    WAVE = struct.unpack_from("4s", data, 8)[0]
    FMT = struct.unpack_from("3s", data, 12)[0]
    TYPE = struct.unpack_from("h", data, 20)[0]
    CHANNELS = struct.unpack_from("h", data, 22)[0]
    RATE = struct.unpack_from("i", data, 24)[0]
    BITS = struct.unpack_from("h", data, 34)[0]
    DATA = struct.unpack_from("4s", data, 36)[0]
    DATA_SIZE = struct.unpack_from("i", data, 40)[0]
    if any((RIFF != b"RIFF", WAVE != b"WAVE", FMT != b"fmt", DATA != b"data")):
        raise Exception
except:
    print("NO")
else:
    print(f'Size={SIZE}, Type={TYPE}, Channels={CHANNELS}, Rate={RATE}, Bits={BITS}, Data size={DATA_SIZE}')

