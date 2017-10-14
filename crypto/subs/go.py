#!/usr/bin/python


cipher_alphabet = {"A": "G", "B": "L", "C": "K", "D": "J", "E": "H",
                   "F": "R", "G": "D", "H": "S", "I": "A", "J": "Z",
                   "K": "X", "L": "C", "M": "V", "N": "B", "O": "N",
                   "P": "M", "Q": "I", "R": "E", "S": "O", "T": "P",
                   "U": "I", "V": "Y", "W": "T", "X": "Q", "Y": "W",
                   "Z": "F"
    }

plaintext = '''This is a very cool plaintext, such wow, such crypto. Substitution ciphers have
been a very popular way of encrypting texts since the beginning of crypography.
However, substitution ciphers have some flaws, namley, you can crack a ciphertext
with frequency analysis. That is probably how you encrypted this text. By analysing
the frequency of characters found in a ciphertext, you can match the frequency found
with the frequency of characters in the english language. This technique works for
any language as long as you have a frequency list for each character in your
particular language. Your flag is Awesome Crypto Novice.'''.upper()

ciphertext = ""

for letter in plaintext:
    if cipher_alphabet.has_key(letter):
        ciphertext += cipher_alphabet.get(letter)
    else:
        ciphertext += letter

print(ciphertext)
