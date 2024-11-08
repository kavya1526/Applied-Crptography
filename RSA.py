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
    # Collect inputs from the user
    pe = int(input("Enter the value for pe: "))
    pc = int(input("Enter the value for pc: "))
    qe = int(input("Enter the value for qe: "))
    qc = int(input("Enter the value for qc: "))
    ee = int(input("Enter the value for ee: "))
    ec = int(input("Enter the value for ec: "))
    encrypted_message = int(input("Enter the encrypted message (as an integer): "))
    plaintext_message = int(input("Enter the plaintext message to encrypt (as an integer): "))

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

    print(f"Decrypted Plaintext: {decrypted_result}")
    print(f"Encrypted Ciphertext: {encrypted_result}")
