#!/usr/bin/python3
from Crypto.Cipher import AES

# Padding for the input string --not
# related to encryption itself.
BS = 16  # Bytes
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]

class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, raw):
        """
        Returns hex encoded encrypted value!
        """
        raw = pad(raw)
        cipher = AES.new(self.key, AES.MODE_CBC)
        encrypted = cipher.encrypt(raw.encode())
        # print(type(msg))
        return encrypted.hex() # .encode('hex')
 
    def decrypt(self, enc):
        """
        Requires hex encoded param to decrypt
        """
        enc = bytes.fromhex(enc) # .decode('hex')
        cipher = AES.new(self.key, AES.MODE_ECB)
        decrypted = cipher.decrypt(enc)

        return unpad(decrypted.decode())

key = b'abcdefghijklmnop'
msg = 'Hackfest0x05_selaludihati'
 
c = AESCipher(key)
ciphertext = c.encrypt(msg)
plaintext = c.decrypt(ciphertext)
print("Ini adalah Ciphertextnya : ", ciphertext)
print("Ini adalah Plaintextnya  : ", plaintext)