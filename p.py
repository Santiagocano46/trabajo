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


import unittest


class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.key = os.urandom(32)
        self.message = "Este es un mensaje secreto"

    def test_encrypt_decrypt(self):
        encrypted_message = encrypt_message(self.message, self.key)
        decrypted_message = decrypt_message(encrypted_message, self.key)
        self.assertEqual(self.message, decrypted_message)

    def test_different_keys(self):
        encrypted_message = encrypt_message(self.message, self.key)
        different_key = os.urandom(32)
        decrypted_message = decrypt_message(encrypted_message, different_key)
        self.assertNotEqual(self.message, decrypted_message)
        self.assertEqual(decrypted_message, "Error: Decryption failed")

    def test_invalid_key_length(self):
        invalid_key = os.urandom(15)
        with self.assertRaises(ValueError):
            encrypt_message(self.message, invalid_key)


if __name__ == "__main__":
    unittest.main()