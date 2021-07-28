from python_crc16 import crc16

#valida un paquete con crc correcto
def test_crc16():
    byte_array_data = bytearray.fromhex('01 01 01 01 01 01 02 00 03 00 03 00 03 00 04 00 04 00 04 00 05 06 07 08 00 00 00 09 00 00 00 0A')
    assert hex(crc16(byte_array_data, 0, 32)) == '0x59c5' 

#valida un paquete con crc correcto
def test_crc16_paquete_vacio():
    byte_array_data = bytearray()
    assert crc16(byte_array_data, 0, 32) == 0
