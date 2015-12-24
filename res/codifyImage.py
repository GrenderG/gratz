import base64
import binascii
 
with open("qrmv.png", "rb") as imageFile:
    codedImage = base64.b64encode(imageFile.read())
    open('xmas-present', 'w').write(bin(int(binascii.hexlify(codedImage), 16)))