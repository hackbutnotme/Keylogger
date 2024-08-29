from cryptography.fernet import Fernet
import sys 

with open('key.key', 'rb') as f:
    key = f.read()
    
cipher_suite = Fernet(key)

with open('klogs.txt', 'rb') as f:
    encrypted_logs = f.readlines()
    
decrypted_logs = ''
for log in encrypted_logs:
    decrypted_log = cipher_suite.decrypt(log.strip()).decode()
    decrypted_logs += decrypted_log + '\n'

with open('decrypted_logs.txt','w') as f:
   f.write(decrypted_logs)

print("Decryption complete.")
sys.exit(0)
    
    
