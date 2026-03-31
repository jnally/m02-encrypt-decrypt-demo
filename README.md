# Module 2: Assignment - Encrypt/Decrypt Demo
**Author:** Jeremy Nally  
**Course:** SDEV245 - Security and Secure Coding  

## Code Functionality Overview
This Python script is an interactive command-line application that demonstrates the core mathematical principles of both symmetric and asymmetric cryptography by building the algorithms entirely from scratch. 

* **Symmetric Encryption (Vigenère Cipher):** Demonstrates symmetric cryptography using a single shared secret key. The code cleans user input using regular expressions, maps letters and spaces to a base-27 numeric dictionary, and uses modular addition with the shared key to encrypt the message. Decryption reverses this exact process using modular subtraction.

* **Asymmetric Encryption (Toy RSA):** Demonstrates public-key cryptography using a mathematically linked key pair. The script programmatically generates prime numbers to calculate a modulus and Euler's totient. It derives a public key for encryption and a private key for decryption, utilizing modular exponentiation to secure and reveal the user's encoded message.
