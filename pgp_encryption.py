import os
import gnupg
from pprint import pprint


sudo apt-get install gnupg
pip install python-gnupg 

################################################################################################
# genrate a key
################################################################################################

#create a folder to store all the genrated keys
#give that path to gpg
gpg = gnupg.GPG(gnupghome='/home/kundan/crypto_file/gnupg')

#create the key credentials
input_data = gpg.gen_key_input(
    name_email='testgpguser@mydomain.com',
    passphrase='testing')

#genrate the key
key = gpg.gen_key(input_data)

#print the key
print (key)


################################################################################################
# encrypt the file using the above key
################################################################################################

#set the key folder path
gpg = gnupg.GPG(gnupghome='/home/kundan/crypto_file/gnupg')

#create a file
open('my-unencrypted.txt', 'w').write('You need to Google Venn diagram.')

# read that file as bytes 
with open('my-unencrypted.txt', 'rb') as f:
    # add recipients value as name_email that you gave while creating the key and encrypt file witha new name
    status = gpg.encrypt_file(
        f, recipients=['testgpguser@mydomain.com'],
        output='my-encrypted.txt.gpg')

#print all the status
print ('ok: ', status.ok)
print ('status: ', status.status)
print ('stderr: ', status.stderr)


################################################################################################
# decrypt the file using the above key
################################################################################################

#set the key folder path
gpg = gnupg.GPG(gnupghome='/home/kundan/crypto_file/gnupg')

#read encrypted file as bytes
with open('my-encrypted.txt.gpg', 'rb') as f:
    #decrypted using the  passphrase values that is given while creating the key
    status = gpg.decrypt_file(f, passphrase='testing', output='my-decrypted.txt')

#print all the status
print ('ok: ', status.ok)
print ('status: ', status.status)
print ('stderr: ', status.stderr)


################################################################################################
# exporting public and private key to other system
################################################################################################


gpg = gnupg.GPG(gnupghome='/home/kundan/crypto_file/gnupg')
ascii_armored_public_keys = gpg.export_keys(str(key), passphrase='testing')
ascii_armored_private_keys = gpg.export_keys(str(key), True, passphrase='testing')
with open('mykeyfile.asc', 'w') as f:
    f.write(ascii_armored_public_keys)
    f.write(ascii_armored_private_keys)


################################################################################################
# import public and private key to other system
################################################################################################

gpg = gnupg.GPG(gnupghome='/home/kundan/crypto_file/gnupg')
key_data = open('PrivateKey.txt').read()
import_result = gpg.import_keys(key_data)
pprint(import_result.results)


