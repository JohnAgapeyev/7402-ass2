#!/usr/bin/python3

import math
import sys
import enchant
import time
import itertools
from multiprocessing import Pool

def decryptMessage(key, message):
    # Determine the number of columns
    nCols = math.ceil(len(message) / key)
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

def try_key(args):
    key, ciphertext = args
    count = 0
    for word in decryptMessage(key, ciphertext).split():
        if len(word) > 5 and dictionary.check(word):
            count += 1
    return count

if len(sys.argv) != 3:
    print('Usage: ./main.py <plaintext_filename> <keysize>')
    sys.exit(1)

data = open(sys.argv[1]).read()
keylen = int(sys.argv[2])
if keylen <= 0:
    print('Key size must be greater than zero')
    sys.exit(1)

dictionary = enchant.Dict("en_US")

ciphertext = encryptMessage(keylen, data)

print("Length of the ciphertext: ", len(ciphertext))

res_list = Pool().map(try_key, zip(range(1, len(ciphertext)), itertools.repeat(ciphertext)))
best_key = res_list.index(max(res_list)) + 1

print(decryptMessage(best_key, ciphertext))
print("Best key was", best_key)
