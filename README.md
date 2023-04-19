# zencrypt
Zencrypt is a simple file encryption and decryption tool that helps protect your files using strong symmetric cryptography. It uses the Fernet encryption scheme, which is based on AES with 128-bit keys in CBC mode and HMAC using SHA256 for authentication.


## Features

- Encrypts and decrypts files in the current directory
- Encrypts file names to protect against casual observation
- Stores encrypted files with a `.zencrypt` extension and a random string in the file name
- Stores keys and encrypted file names in a key file located at `/root/keys/key.key`

## Installation

1. Clone the repository:
```
  git clone https://github.com/yourusername/zencrypt.git
```  
2. Navigate to the zencrypt directory:
```
  cd zencrypt
```
3. Run the installation script:
```
  sudo ./install.sh
``` 
  This will create the `/root/keys` directory, move the `zencrypt.py` script to `/root/keys/encrypt.py`, and move the `zencrypt` shell script to `/sbin/zencrypt`.

## Usage

To encrypt files in the current directory, simply run:
```
  sudo zencrypt
```

To decrypt files in the current directory, use the `--decrypt` or `-d` option:
```
  sudo zencrypt -d
```  

## Tip

  zencrypt can be used recursively over and over on the same files
  
## Warning

Losing the key file located at `/root/keys/key.key` will make it nearly impossible to restore the encrypted files. To avoid this risk, consider backing up the key file to a secure location, such as an encrypted USB drive, external hard drive, or secure cloud storage.


This project is  designed for linux machines only and it is based on the assumption that the root folder is secured
