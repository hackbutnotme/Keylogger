from cryptography.fernet import Fernet

with open('key.key', 'rb') as f:
    key = f.read()
    
cipher_suite = Fernet(key)

with open('klogs.txt', 'rb') as f:
    encrypted_logs = f.readlines()
    
decrypted_logs = []
decrypted_logs = cipher_suite.decrypt(encrypted_logs)

with open('decrypted_logs.txt','w') as f:
   f.write(decrypted_logs.decode())
    
    
