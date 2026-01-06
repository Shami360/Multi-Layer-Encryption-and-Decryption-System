print("Multi-Layer Encryption Project")

# ---------------- Caesar Cipher ----------------
def caesar_encrypt(text, shift):
    encrypted = ""
    for ch in text:
        if ch.isalpha():
            encrypted += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            encrypted += ch
    return encrypted


def caesar_decrypt(text, shift):
    decrypted = ""
    for ch in text:
        if ch.isalpha():
            decrypted += chr((ord(ch) - 65 - shift) % 26 + 65)
        else:
            decrypted += ch
    return decrypted


# ---------------- Transposition (Safe) ----------------
def transpose(text):
    return text[::-1]          # reverse string


def reverse_transpose(text):
    return text[::-1]          # reverse back


# ---------------- Vernam Cipher ----------------
def generate_key(text):
    key = ""
    base_key = "SECUREKEY"
    for i in range(len(text)):
        key += base_key[i % len(base_key)]
    return key


def vernam_encrypt(text, key):
    cipher = ""
    for t, k in zip(text, key):
        cipher += chr(((ord(t) - 65 + ord(k) - 65) % 26) + 65)
    return cipher


def vernam_decrypt(cipher, key):
    plain = ""
    for c, k in zip(cipher, key):
        plain += chr(((ord(c) - 65 - (ord(k) - 65)) % 26) + 65)
    return plain


# ---------------- MAIN PROGRAM ----------------
plain_text = "Faisal".upper()
print("\nPlain Text:", plain_text)

# Layer 1: Caesar
caesar_text = caesar_encrypt(plain_text, 3)
print("After Caesar Cipher:", caesar_text)

# Layer 2: Transposition
transposed_text = transpose(caesar_text)
print("After Transposition:", transposed_text)

# Layer 3: Vernam
key = generate_key(transposed_text)
print("Generated Key:", key)

cipher_text = vernam_encrypt(transposed_text, key)
print("Final Encrypted Text:", cipher_text)

# ---------------- DECRYPTION ----------------
print("\n--- DECRYPTION PROCESS ---")

step1 = vernam_decrypt(cipher_text, key)
print("After Vernam Decryption:", step1)

step2 = reverse_transpose(step1)
print("After Reverse Transposition:", step2)

final_text = caesar_decrypt(step2, 3)
print("Final Decrypted Text:", final_text)
