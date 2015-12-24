import binascii

fh = open('xmas-presents.png', 'wb')
decoded_string = open('xmas-present', 'rb').read()
n = int(decoded_string, 2)
fh.write(binascii.unhexlify('%x' % n).decode('base64'))
fh.close()