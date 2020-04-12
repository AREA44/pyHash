# Python rogram to find the MD5, SHA-1 and SHA-256 message digest of a file

import hashlib

filename = input("Location of the file: ")
# The size of each read from the file
BLOCK_SIZE = 65536

# Make a hash object
md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha256 = hashlib.sha256()

# Open file for reading in binary mode
with open(filename,'rb') as f:

    # Read from the file
    chunk = f.read(BLOCK_SIZE)

    # While there is still data being read from the file
    while len(chunk) > 0:
        # Update the hash
        md5.update(chunk)
        sha1.update(chunk)
        sha256.update(chunk)
        # Read the next block from the file
        chunk = f.read(BLOCK_SIZE)

# Print the hex representation of digest
print("MD5: " + md5.hexdigest()
    + "\nSH1: " + sha1.hexdigest()
    + "\nSHA256: " + sha256.hexdigest())