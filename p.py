from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def encrypt_message(message, key):
    valid_lengths = [16, 24, 32]
    if len(key) not in valid_lengths:
        raise ValueError("Invalid key length. Key must be 16, 24, or 32 bytes long.")

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()

    encrypted_message = encryptor.update(padded_data) + encryptor.finalize()

    return iv + encrypted_message

def decrypt_message(encrypted_message, key):
    try:
        iv = encrypted_message[:16]
        actual_encrypted_message = encrypted_message[16:]

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        decrypted_padded_message = decryptor.update(actual_encrypted_message) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        decrypted_message = unpadder.update(decrypted_padded_message) + unpadder.finalize()

        return decrypted_message.decode()

    except (ValueError, Exception):
        return "Error: Decryption failed"

# Función principal
def main():
    operation = input("¿Qué operación deseas realizar? (encrypt/decrypt): ").lower()

    if operation not in ['encrypt', 'decrypt']:
        print("Operación no válida. Por favor, elige 'encrypt' o 'decrypt'.")
        return

    message = input("Introduce el mensaje: ")

    # El usuario debe ingresar una clave de longitud válida (16, 24 o 32 bytes)
    key_input = input("Introduce la clave (16, 24 o 32 caracteres): ")
    key = key_input.encode()

    if operation == 'encrypt':
        try:
            encrypted_message = encrypt_message(message, key)
            print(f"Mensaje encriptado (hex): {encrypted_message.hex()}")
        except ValueError as e:
            print(f"Error: {e}")

    elif operation == 'decrypt':
        encrypted_message_input = input("Introduce el mensaje encriptado (en formato hexadecimal): ")
        encrypted_message = bytes.fromhex(encrypted_message_input)

        decrypted_message = decrypt_message(encrypted_message, key)
        print(f"Mensaje desencriptado: {decrypted_message}")

if __name__ == "__main__":
    main()
