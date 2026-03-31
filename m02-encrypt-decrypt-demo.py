import random
import math
import re

# quick and non-optimized prime checker
def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**.5) + 1, 2):
        if number % i == 0:
            return False
    return True

# generate a random prime between given values
def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime

# find modular multiplicative inverse
def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError('mod_inverse does not exist')

# demonsrate RSA encryption and decryption
def rsa_demo():
    # generate two distinct primes
    p, q = generate_prime(1000, 5000), generate_prime(1000, 5000)
    while p == q:
        q = generate_prime(1000, 5000)
    print('\nRSA requires two distinct primes.')
    print('p: ', p)
    print('q: ', q)

    # generate n
    print('\nFind product of primes.')
    n = p * q
    print('n: ', n)

    # Euler's totient function
    print('\nFind Euler\'s totient function phi(n) = (p - 1)(q - 1).')
    phi_n = (p - 1) * (q - 1)
    print('phi(n): ',phi_n)
    

    # generate public key
    print('\nGenerate public by finding random relatively prime number between 3 and phi(n) - 1.')
    e = random.randint(3, phi_n - 1)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(3, phi_n - 1)
    print("Public Key (e): ", e)

    # generate private key
    print('\nGenerate private key by finding modular multiplicative inverse of public key with respect to phi(n).')
    d = mod_inverse(e, phi_n)
    print("Private Key (d): ", d)

    message = input('\nInput a message to be encoded and encrypted: ')

    # ord returns unicode for character
    print('\nEncode message into unicode.')
    message_encoded = [ord(ch) for ch in message]
    # (m^e) mod n = c
    print('message_encoded: ',message_encoded)

    print('\nUse public key to encrypt characters in message using (character^e) mod n.')
    message_encrypted = [pow(ch, e, n) for ch in message_encoded]
    # pow(ch, e, n) same as (ch^e) mod n
    print('message_encrypted (output anyone can see, but only someone private key can decrypt): ', message_encrypted)

    print('\nImagine sending the encrypted message to someone with the private key...')

    print('\nUse private key to decrypt message using (character^d) mod n.')
    message_decrypted = [pow(ch, d, n) for ch in message_encrypted]
    print('message_decrypted: ', message_decrypted)
    
    # chr returns character corresponding to unicode
    print('\nDecode message from unicode back to characters.')
    decoded_message = ''.join(chr(ch) for ch in message_decrypted)
    print('decoded_message (output to user with private key only): ', decoded_message)

# letters and space for handmade Vigenere cypher
letters = {'a':0,
           'b':1,
           'c':2,
           'd':3,
           'e':4,
           'f':5,
           'g':6,
           'h':7,
           'i':8,
           'j':9,
           'k':10,
           'l':11,
           'm':12,
           'n':13,
           'o':14,
           'p':15,
           'q':16,
           'r':17,
           's':18,
           't':19,
           'u':20,
           'v':21,
           'w':22,
           'x':23,
           'y':24,
           'z':25,
           ' ':26}

# flip letters around the other way and name it numbers
numbers = dict()
i = 0
for key in letters:
    numbers[i] = key
    i += 1

# Just return lowercase alpha and spaces
def stripNonAlphaMakeLower(message):
    return re.sub('[^a-z ]','',message.lower())

# convert text to numeric list using global variables
def textToNumericList(text):
    numList = []
    text = stripNonAlphaMakeLower(text)
    for c in text:
        numList.append(letters[c])
    return numList

# convert numbers to text using global variables
def numericListToText(numList):
    text = ''
    for n in numList:
        text += numbers[n]
    return text

# use shared key to encrypt message and return nonsense
def vigenereEncrypt(message,key):
    keyLen = len(key)
    keyNum = textToNumericList(key)
    mesNum = textToNumericList(message)
    encMesNum = []
    encMes = ''

    # loop through characters and encrypt
    for i in range(len(mesNum)):
        encMesNum.append((mesNum[i] + keyNum[i % keyLen]) % 27)

    encMes = numericListToText(encMesNum)
    
    return encMes.upper()

# decrypt nonsense message using shared key and return actual message
def vigenereDecrypt(message,key):
    keyLen = len(key)
    keyNum = textToNumericList(key)
    mesNum = textToNumericList(message)
    decMesNum = []
    decMes = ''

    # loop through characters and decrypt
    for i in range(len(mesNum)):
        decMesNum.append((mesNum[i] - keyNum[i % keyLen]) % 27)
        #print(mesNum[i] - keyNum[i % keyLen], (mesNum[i] - keyNum[i % keyLen]) % 27, numbers[(mesNum[i] - keyNum[i % keyLen]) % 27])

    decMes = numericListToText(decMesNum)
    
    return decMes.lower()

# Vigenere demo
def vigenere_demo():
    key = input('\nCreate a key word to share with an ally: ')
    message = input('Create a message to send to an ally with the key: ')
    encrypted_message = vigenereEncrypt(message, key)
    
    print('\nImagine you are the ally now...')

    print('You just received the following message: ', encrypted_message)
    new_key = input('\nEnter the key that your ally told you about: ')
    decrypted_message = vigenereDecrypt(encrypted_message, new_key)
    print('The message decrypted to: ', decrypted_message)


# run both demos
def main():
    print('Module 2: Assignment - Encrypt/Decrypt Demo')
    print('\nVigenere Demo - Symmetric Encryption')
    vigenere_demo()

    input('\n\n\nPress enter to continue.')
    
    print('\n\n\nRSA Demo - Asymmetric Encryption')
    rsa_demo()

# execute main function
if __name__ == '__main__':
    main()
