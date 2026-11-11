"""소년이 달리는 수업 장면 위에 새 10마리의 비행을 표시한다."""

from pico2d import close_canvas, open_canvas

import game_framework
import play_mode
from settings import CANVAS_HEIGHT, CANVAS_WIDTH


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        game_framework.run(play_mode)
    finally:
        close_canvas()


if __name__ == '__main__':
    main()
