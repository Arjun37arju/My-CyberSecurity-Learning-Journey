from cryptography.fernet import Fernet
key=Fernet.generate_key()    # this portion make the key .. this key kept in secrete
cipher=Fernet(key)           # this make the cipher text

message=b"hello ,this is secrete"
encrypted=cipher.encrypt(message)
decrypted=cipher.decrypt(encrypted)

print("key : ",key)
print("original :",message)
print("Encryption :",encrypted)
print("Decryption :",decrypted)
