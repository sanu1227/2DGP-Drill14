import time
from pico2d import delay
from settings import TARGET_FPS
running = False
stack = []


def change_mode(mode):
    if stack:
        stack.pop().finish()
    stack.append(mode)
    mode.init()


def push_mode(mode):
    if stack:
        stack[-1].pause()
    stack.append(mode)
    mode.init()


def pop_mode():
    if stack:
        stack.pop().finish()
    if stack:
        stack[-1].resume()
    else:
        quit()


def quit():
    global running
    running = False

frame_time = 0.0

def run(start_mode):
    global running, stack, frame_time
    running = True
    stack = [start_mode]

    try:
        start_mode.init()
        frame_time = 0.0
        previous_time = time.perf_counter()
        while running:
            frame_start = time.perf_counter()
            frame_time = frame_start - previous_time
            previous_time = frame_start
            stack[-1].handle_events()
            if not running or not stack:
                break
            stack[-1].update()
            stack[-1].render()
            remaining = 1.0 / TARGET_FPS - (time.perf_counter() - frame_start)
            if remaining > 0:
                delay(remaining)
    finally:
        while stack:
            stack.pop().finish()
        running = False
