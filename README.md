# CRC-16/CCITT-FALSE

Python implementation CRC-16/CCITT-FALSE algorithm used by nordic SDK

* Poly 0x1021	
* Init 0xFFFF

# Requirements

```bash
sudo pip3 install -r requirements.txt
```

# Testing

```bash
./test.sh
```

# Usage Example

```python
crc16(data : bytearray, offset , length):
```

```python
hex(crc16(b'\x01\x02\x03\x04', 0, 4))
'0x89c3'
```