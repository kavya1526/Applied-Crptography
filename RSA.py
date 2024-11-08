import sys
from math import gcd

# Extended Euclidean Algorithm to find modular inverse
def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    gcd_val, x_prev, y_prev = extended_euclidean(b % a, a)
    x_current = y_prev - (b // a) * x_prev
    y_current = x_prev
    return gcd_val, x_current, y_current

# Function to generate the private key (d)
def generate_private_key(e, p, q):
    phi = (p - 1) * (q - 1)
    gcd, x, _ = extended_euclidean(e, phi)
    if gcd != 1:
        raise ValueError("e and phi(n) are not coprime")
    d = x % phi
    return d

# Function to encrypt a plaintext message
def encrypt(plaintext, e, n):
    ciphertext = pow(int(plaintext), e, n)
    return str(ciphertext)

# Function to decrypt a ciphertext message
def decrypt(ciphertext, d, n):
    plaintext = pow(int(ciphertext), d, n)
    return str(plaintext)

# Main function to handle CLI input and perform encryption/decryption
if __name__ == "__main__":
    # Collect inputs from the command line
    pe = int(sys.argv[1])
    pc = int(sys.argv[2])
    qe = int(sys.argv[3])
    qc = int(sys.argv[4])
    ee = int(sys.argv[5])
    ec = int(sys.argv[6])
    encrypted_message = int(sys.argv[7])
    plaintext_message = int(sys.argv[8])

    # Compute p, q, and e values
    p = (2 ** pe) - pc
    q = (2 ** qe) - qc
    e = (2 ** ee) - ec
    n = p * q

    # Generate private key
    d = generate_private_key(e, p, q)

    # Encrypt and decrypt
    encrypted_result = encrypt(plaintext_message, e, n)
    decrypted_result = decrypt(encrypted_message, d, n)

    # Output the result in the required format
    print(f"{decrypted_result},{encrypted_result}")
