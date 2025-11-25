import time
import random
from pynput import keyboard, mouse
from pynput.keyboard import Key, Controller

IDLE_LIMIT = 8  # seconds
last_activity = time.time()
paused = False
running = True

kb_controller = Controller()


# -----------------------
# YOUR ACTIONS
# -----------------------
def alt_tab():
    kb_controller.press(Key.alt)
    kb_controller.tap(Key.tab)
    kb_controller.tap(Key.tab)
    kb_controller.release(Key.alt)
    print("ALT + TAB sent!")


def alt_ctrl():
    kb_controller.press(Key.ctrl)
    kb_controller.tap(Key.tab)
    print("ALT + CTRL + TAB sent!")


actions = [alt_tab, alt_ctrl]


# -----------------------
# IDLE RESET
# -----------------------
def reset_idle(*_):
    global last_activity
    if not paused:
        last_activity = time.time()


# -----------------------
# KEYBOARD HOTKEYS
# -----------------------
def on_key_press(key):
    global paused, running, last_activity

    # Always detect ESC
    if key == keyboard.Key.esc:
        running = False
        return

    # Pause
    if key == keyboard.Key.f8:
        paused = True
        print("Paused.")
        return

    # Resume
    if key == keyboard.Key.f9:
        paused = False
        last_activity = time.time()  # reset idle when resuming
        print("Resumed.")
        return

    reset_idle()


# -----------------------
# MOUSE LISTENERS
# -----------------------
def on_mouse_event(*_):
    reset_idle()


# -----------------------
# MAIN LOOP (VERY LIGHTWEIGHT)
# -----------------------
print("Monitoring activity... F8 = pause, F9 = resume, ESC = exit")

kb_listener = keyboard.Listener(on_press=on_key_press)
mouse_listener = mouse.Listener(
    on_move=on_mouse_event, on_click=on_mouse_event, on_scroll=on_mouse_event
)

kb_listener.start()
mouse_listener.start()

while running:
    if not paused and (time.time() - last_activity) >= IDLE_LIMIT:
        random.choice(actions)()
        last_activity = time.time()
    time.sleep(0.2)  # Extremely low CPU usage
