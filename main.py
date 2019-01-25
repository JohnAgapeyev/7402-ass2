#!/usr/bin/python3

import math
import sys

def decryptMessage(key, message):
    # Determine the number of columns
    nCols = math.ceil (len (message) / key)
    # Determine the number of rows
    nRows = key
    # Determine the unused cells
    nUnused = (nCols * nRows) - len(message)
    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * nCols
    # row and col point to the location of the next character in the ciphertext
    row = col = 0
    for symbol in message:
        plaintext[col] += symbol
        col += 1 # point to next column
        # If it reaches the last column in the row, or at an unused cell, start processing the next row
        if (col == nCols) or (col == nCols - 1 and row >= nRows - nUnused):
            col = 0
            row += 1
    return ''.join(plaintext)

def encryptMessage (key, message):
    # Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key
    # Iterate through each column in ciphertext.
    for col in range (key):
        pointer = col

        # process the complete length of the plaintext
        while pointer < len (message):
            # Place the character at pointer in message at the end of the
            # current column in the ciphertext list.
            ciphertext[col] += message[pointer]
            # move pointer over
            pointer += key
    # Convert the ciphertext list into a single string value and return it.
    return ''.join (ciphertext)

if len(sys.argv) != 3:
    print('Usage: ./main.py <plaintext_filename> <keysize>')
    sys.exit(1)
data = open(sys.argv[1]).read()
keylen = int(sys.argv[2])

print("Data is {}", data)

# call the crypto function
ciphertext = encryptMessage(keylen, data)
plaintext = decryptMessage(keylen, ciphertext);
# Print the ciphertext
print(plaintext)

