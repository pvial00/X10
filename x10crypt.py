from x10 import X10
from pycube256 import CubeRandom, CubeKDF
import sys, select, getpass, os, time, getopt, hashlib

mode = sys.argv[1]

input_filename = sys.argv[2]
output_filename = sys.argv[3]

try:
    infile = open(input_filename, "r")
except IOError as ier:
    print "Input file not found."
    sys.exit(1)

try:
    outfile = open(output_filename, "w")
except IOError as ier:
    print "Output file not found."
    sys.exit(1)

try:
    key = sys.argv[4]
except IndexError as ier:
    key = getpass.getpass("Enter key: ")

# 128 bit key size
key = CubeKDF().genkey(key)
nonce_length = 8

start = time.time()
data = infile.read()
infile.close()
if mode == "encrypt":
    nonce = CubeRandom().random(nonce_length)
    cipher_text = X10(key).encrypt(data, nonce)
    outfile.write(nonce+cipher_text)
elif mode == "decrypt":
    nonce = data[:nonce_length]
    msg = data[nonce_length:]
    x2 = X10(key)
    plain_text = x2.decrypt(msg, nonce)
    outfile.write(plain_text)
outfile.close()

end = time.time() - start
bps = len(data) / end
sys.stdout.write("Completed in "+str(end)+" seconds\n")
sys.stdout.write(str(bps)+" bytes per second.\n")
