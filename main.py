def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def binary_to_text(binary):
    text = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    return text

def xor_strings(s1, s2):
    return ''.join(str(int(a) ^ int(b)) for a, b in zip(s1, s2))

def encrypt_decrypt_bbs(text, gamma):
    binary_text = text_to_binary(text)
    gamma = (gamma * (len(binary_text) // len(gamma) + 1))[:len(binary_text)]
    encrypted_decrypted_binary = xor_strings(binary_text, gamma)
    encrypted_decrypted_text = binary_to_text(encrypted_decrypted_binary)
    return encrypted_decrypted_text

