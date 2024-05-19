import PIL.Image as Image
import PIL.ImageGrab
import mss.tools
import pygetwindow as gw
from pywinauto.application import Application
import win32gui as wgui 
import mss
import time
import PIL

def capture_window(title):
    try:
        window = gw.getWindowsWithTitle(title)[0]
        if window:
            window.activate()
            while not window.isActive:
                time.sleep(0.5)
            

            #window.minimize()
            #window.restore()
            #window.wait('ready', timeout=10)
            x, y, width, height = window.left, window.top, window.width, window.height

            rect = window._getWindowRect()

            app = Application().connect(handle=window._hWnd)
            client_area = app.window(handle=window._hWnd).rectangle()
            ca_width = client_area.width()
            ca_height = client_area.height()

            client_rect = app.window(handle=window._hWnd).client_rect()
            cr_w = client_rect.width()
            cr_h = client_rect.height()
            cr_x = client_rect.left
            cr_y = client_rect.top

            print(f"Here coords: {rect}")
            print(f"Versus: top: {y}, left : {x}, width: {width}, height: {height}")
            print(f"Here is inner app: top: {client_area.top}, left: {client_area.left}, width: {ca_width}, height: {ca_height}")
            print(f"Here is width & height: {cr_w}, {cr_h} | {cr_x}, {cr_y}")
            with mss.mss() as sct:
                monitor = {"top": y, "left": x, "width": width, "height": cr_h}
                #monitor_pil = (x, y, a, b)
                #screenshot = PIL.ImageGrab.grab(bbox=monitor_pil)
                screen = sct.grab(monitor)
                img = Image.frombytes("RGB", screen.size, screen.bgra, "raw", "BGRX")
                mss.tools.to_png(screen.rgb, screen.size, output="screenshot.png")
            #screenshot = pyautogui.screenshot(region=(x, y, width, height))
            return img
    except IndexError:
        print(f"No window with title '{title}' found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Need to figure out how to get the screenshots working as intended without the top bar,
# because the OCR picks up the file & GBA stuff, which then in turn affects the translation output.
# This is currently somewhat remedied by trying to tell gpt to not pay attention to clumped english text, but it has variable results.
# I also need to figure out a polling rate, perhaps I can tie it to 3 seconds after the key press? 
# Then I need to actually display the translated text... maybe just output to a gui - that seems most simple, & she has two monitors, possibly.
# I could do that then make more efforts to actually make the UI look better/more implementation. 
# The base of the work is done now though, just need to do the (I think hardest part) UI. But most of the backend is done.
# I think a simple UI should be good enough? But we'll see how crazy we can get.
# Also need to remember to implement the actual choosing of a window. That part could get complicated. Alt solution is put it on person to make the name/type the name in a txt file possibly...
# Or maybe I could put it into a txt file instead of having to use a gui? Will have to research more