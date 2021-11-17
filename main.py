import threading
import mouse
import keyboard
from time import time, sleep
import pickle


def play_events(keyboard_events, mouse_events):
    # Use threading to play mouse and keyboards events simultaneously:
    # Keyboard threadings:
    k_thread = threading.Thread(target=lambda: keyboard.play(keyboard_events))
    k_thread.start()

    # Mouse threadings:
    m_thread = threading.Thread(target=lambda: mouse.play(mouse_events))
    m_thread.start()

    # Waiting for both threadings to be completed
    k_thread.join()
    m_thread.join()


def record_keyboard_and_mouse():
    mouse_events = []
    mouse.hook(mouse_events.append)
    keyboard.start_recording()  # Starting the recording
    sleep(60)
    mouse.unhook(mouse_events.append)
    keyboard_events = keyboard.stop_recording()  # Stopping the recording. Returns list of events
    print('stop recording keyboard and mouse events, returning events...')

    time_str = str(int(time()))

    if len(keyboard_events) >= 10:
        pickle.dump(keyboard_events, open(f'keyboard_events{time_str}.pickle', 'wb'))
        pickle.dump(mouse_events, open(f'mouse_events{time_str}.pickle', 'wb'))


if __name__ == '__main__':
    print('start recording keyboard and mouse events...')
    while (True):
        record_keyboard_and_mouse()
