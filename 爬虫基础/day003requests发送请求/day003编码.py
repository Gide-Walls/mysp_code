str_code="abc"
print(type(str_code))


byte_code=str_code.encode()
print(type(byte_code))


byte_code=b"abcd"
print(type(byte_code))
str_code=byte_code.decode()
print(type(str_code))