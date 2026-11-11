"""Drill14 새 비행 애니메이션 실행 진입점."""

from time import perf_counter

from pico2d import (
    SDL_KEYDOWN, SDL_QUIT, SDLK_ESCAPE,
    clear_canvas, close_canvas, delay, get_events, open_canvas, update_canvas,
)

from flock import Flock
from settings import CANVAS_HEIGHT, CANVAS_WIDTH, TARGET_FPS


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    flock = None
    try:
        flock = Flock()
        previous_time = perf_counter()
        running = True
        while running:
            frame_start = perf_counter()
            dt = frame_start - previous_time
            previous_time = frame_start
            for event in get_events():
                if event.type == SDL_QUIT or (
                    event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
                ):
                    running = False
            if not running:
                break
            flock.update(dt)
            clear_canvas()
            flock.draw()
            update_canvas()
            # 남은 시간만 대기한다. 이동과 날갯짓은 실제 경과 시간을 사용한다.
            remaining = 1.0 / TARGET_FPS - (perf_counter() - frame_start)
            if remaining > 0:
                delay(remaining)
    finally:
        # SDL 렌더러를 닫기 전에 새들과 공유 텍스처 참조를 해제한다.
        flock = None
        close_canvas()


if __name__ == '__main__':
    main()
