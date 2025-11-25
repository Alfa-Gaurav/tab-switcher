import random
from pynput.keyboard import Key, Controller

kb_controller = Controller()


# -----------------------
# YOUR ACTIONS
# -----------------------
def alt_tab():
    kb_controller.press(Key.alt)
    kb_controller.tap(Key.tab)
    kb_controller.tap(Key.tab)
    kb_controller.tap(Key.tab)
    kb_controller.tap(Key.tab)
    kb_controller.release(Key.alt)
    print("ALT + TAB sent!")


def alt_ctrl():
    kb_controller.press(Key.ctrl)
    kb_controller.tap(Key.tab)
    kb_controller.release(Key.ctrl)
    print("CTRL + TAB sent!")


actions = [alt_tab, alt_ctrl]

if __name__ == "__main__":
    action = random.choice(actions)
    action()
    print("Exiting...")
