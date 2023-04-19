#!/usr/bin/env python3
import sys
import os
import argparse
import uuid
from cryptography.fernet import Fernet

KEY_FILE_PATH = '/root/keys/key.key'

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(data)
    encrypted_file_name = f'{uuid.uuid4().hex}.zencrypt'
    encrypted_file_path = os.path.join(os.path.dirname(file_path), encrypted_file_name)
    with open(encrypted_file_path, 'wb') as file:
        file.write(cipher_text)
    return encrypted_file_name

def decrypt_file(encrypted_file_path, decrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as file:
        data = file.read()
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(data)
    with open(decrypted_file_path, 'wb') as file:
        file.write(plain_text)

def main():
    parser = argparse.ArgumentParser(description='Encrypt or decrypt files in the current directory.')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt files instead of encrypting')
    args = parser.parse_args()

    keys = {}

    if os.path.exists(KEY_FILE_PATH):
        with open(KEY_FILE_PATH, 'r') as key_file:
            for line in key_file:
                try:
                    encrypted_file_name,file_path, file_key = line.strip().split('\t')
                    keys[encrypted_file_name] = (file_path, file_key)
                except ValueError:
                    print(f'Invalid line in key file: {line.strip()}')

    current_directory = os.getcwd()
    for file_name in os.listdir(current_directory):
        file_path = os.path.join(current_directory, file_name)

        if file_name == sys.argv[0] or file_path == KEY_FILE_PATH:
            continue

        if not args.decrypt:
            if file_path not in keys:
                key = generate_key()
                encrypted_file_name = encrypt_file(file_path, key)
                keys[encrypted_file_name] = (file_path, key.decode())
                os.remove(file_path)
            else:
                print(f'everything is already encrypted.')
        else:
            if file_name in keys:
                encrypted_file_name=file_name
                file_path, file_key = keys[encrypted_file_name]
                encrypted_file_path = os.path.join(current_directory, encrypted_file_name)
                key = file_key.encode()
                decrypt_file(encrypted_file_path, file_path, key)
                os.remove(encrypted_file_path)
                del keys[encrypted_file_name]
            else:
                print(f'{file_path} is not encrypted or key is missing.')

    with open(KEY_FILE_PATH, 'w') as key_file:
        for encrypted_file_name, (file_path, file_key) in keys.items():
            key_file.write(f'{encrypted_file_name}\t{file_path}\t{file_key}\n')

if __name__ == '__main__':
    main()
