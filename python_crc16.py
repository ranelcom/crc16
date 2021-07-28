def crc16(data : bytearray, offset , length):
    if data is None or offset < 0 or offset > len(data)- 1 and offset+length > len(data):
        return 0
    crc = 0xFFFF
    for i in range(0, length):
        crc ^= data[offset + i] << 8
        for j in range(0,8):
            if (crc & 0x8000) > 0:
                crc =(crc << 1) ^ 0x1021
            else:
                crc = crc << 1
    return crc & 0xFFFF

def main(): # pragma: no cover
    #crc16 packet must be 0x59C5
    byte_array_data = bytearray.fromhex('01 01 01 01 01 01 02 00 03 00 03 00 03 00 04 00 04 00 04 00 05 06 07 08 00 00 00 09 00 00 00 0A')
    print("Calculating CRC16/CCITT-FALSE from packet:", byte_array_data)
    modified_data = crc16(byte_array_data, 0, 32)
    print( "CRC16/CCITT-FALSE: ", hex(modified_data))

if __name__ == "__main__": # pragma: no cover
    main()
