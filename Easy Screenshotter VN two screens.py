import pyautogui
from io import BytesIO
import win32clipboard
from pynput.keyboard import Listener  as KeyboardListener
from pynput.mouse    import Listener  as MouseListener
from pynput.keyboard import Key
from pynput.mouse import Button




def send_to_clipboard(image):
    output = BytesIO()
    image.convert('RGB').save(output, 'BMP')
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

def screenshot():
	image = pyautogui.screenshot()
	send_to_clipboard(image)



screenWidth, screenHeight = pyautogui.size()


pyautogui.alert('BlackSwallowtail\'s easy screenshot tool')


global skip
skip = False

def on_press(key):
	if key == Key.alt_l:
		screenshot()


def on_click(x, y, button, pressed):
	return


with MouseListener(on_click=on_click) as listener:
	with KeyboardListener(on_press=on_press) as listener:
		listener.join()









