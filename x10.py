class X10:
    def __init__(self, key):
        k = ""
        for byte in key:
            k += str(ord(byte))
        self.key = int(k)

    def encrypt(self, data, nonce=""):
        buf = ""
        for byte in data:
            buf += "2" + str('%03d' % ord(byte))
        n = ""
        n2 = 0
        for byte in nonce:
            n += "2" + str('%03d' % ord(byte))
            n2 += ord(byte)
        c = str((int(buf) * (self.key + (n2 ** 2))) / int(n))
        return c

    def decrypt(self, data, nonce=""):
        n = ""
        n2 = 0
        for byte in nonce:
            n += "2" + str('%03d' % ord(byte))
            n2 += ord(byte)
        c = str((int(data) * int(n)) / (self.key + (n2 ** 2)))
        s = 0
        e = 4
        p = ""
        for x in range(len(c) / 4):
            p += chr(int(c[(s + 1):e]))
            s += 4
            e += 4
        return p
