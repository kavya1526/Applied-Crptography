# RSA Encryption/Decryption Program

This program demonstrates RSA encryption and decryption using Python. It uses the Extended Euclidean Algorithm to find modular inverses and performs encryption and decryption based on RSA principles.

## Requirements

- Python 

## Setup

1. **Clone or download the repository containing this program**.

2. **Navigate to the directory** where the program file is located.

3. **Ensure Python is installed**:
    - You can check if Python is installed by running:
      ```bash
      python --version
      ```
    - If Python is not installed, download it from [Python's official website](https://www.python.org/downloads/).

## Running the Program

The program takes input values for RSA key generation, encryption, and decryption. Follow these steps to execute the program:

1. **Run the program**:
   ```bash
   python3 RSA.py

## Important Notes

1. Ensure **\( p \) and \( q \)** are **prime numbers** for secure RSA encryption. You may need to adjust \( pe \), \( pc \), \( qe \), and \( qc \) to get valid primes.
2. Ensure \( e \) and **phi(n)** (Euler's Totient function of n) are **coprime**. This is essential for generating a valid private key and ensuring secure encryption and decryption.

