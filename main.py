import random
from pynput.keyboard import Key
from pynput.keyboard import Controller


def alt_tab():
    keyboard.press(Key.alt)
    keyboard.tap(Key.tab)
    keyboard.tap(Key.tab)
    keyboard.release(Key.alt)


def alt_ctrl():
    keyboard.press(Key.alt)
    keyboard.press(Key.ctrl)
    keyboard.tap(Key.tab)
    keyboard.release(Key.ctrl)
    keyboard.release(Key.alt)


print("ALT + TAB sent!")


if __name__ == "__main__":
    keyboard = Controller()
    actions = [alt_tab, alt_ctrl]
    action = random.choice(actions)
    action()
