import os
import hashlib
from Crypto.Cipher import AES
from Crypto.Util import Padding

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = in_filename + '.enc'
    iv = os.urandom(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(filesize.to_bytes(8, 'big'))
            outfile.write(iv)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                chunk = Padding.pad(chunk, AES.block_size, style='pkcs7')
                outfile.write(encryptor.encrypt(chunk))

def decrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]
    with open(in_filename, 'rb') as infile:
        original_size = int.from_bytes(infile.read(8), 'big')
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)
        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(original_size)

def encrypt_folder(key, in_folder, out_folder=None):
    if not out_folder:
        out_folder = in_folder + '.enc'
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    for root, dirs, files in os.walk(in_folder):
        for dir in dirs:
            encrypt_folder(key, os.path.join(root, dir), os.path.join(out_folder, dir))
        for file in files:
            encrypt_file(key, os.path.join(root, file), os.path.join(out_folder, file))

def decrypt_folder(key, in_folder, out_folder=None):
    if not out_folder:
        out_folder = os.path.splitext(in_folder)[0]
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    for root, dirs, files in os.walk(in_folder):
        for dir in dirs:
            decrypt_folder(key, os.path.join(root, dir), os.path.join(out_folder, dir))
            for file in files:
                decrypt_file(key, os.path.join(root, file), os.path.join(out_folder, file))
                
                if name == 'main':
                    key = hashlib.sha256('secret_key'.encode()).digest()
                    in_folder = 'example_folder'
                    out_folder = 'encrypted_folder'
                    encrypt_folder(key, in_folder, out_folder)
                    decrypt_folder(key, out_folder)