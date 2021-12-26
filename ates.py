import base64

msg = b"saya"

#ubah base64
b64 = base64.b64encode(msg)
b32 = base64.b32encode(msg)

print(b64)
print(b32)

print(base64.b64decode(b64))
print(base64.b32decode(b32))