"""Drill14 새 비행 애니메이션 실행 진입점."""

from pico2d import (
    SDL_KEYDOWN, SDL_QUIT, SDLK_ESCAPE,
    clear_canvas, close_canvas, delay, get_events, load_image, open_canvas, update_canvas,
)

from bird import Bird
from settings import CANVAS_HEIGHT, CANVAS_WIDTH, TARGET_FPS


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        image = load_image('bird_animation.png')
        bird = Bird(image, CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)
        running = True
        while running:
            for event in get_events():
                if event.type == SDL_QUIT or (
                    event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
                ):
                    running = False
            if not running:
                break
            bird.update(1.0 / TARGET_FPS)
            clear_canvas()
            bird.draw()
            update_canvas()
            delay(1.0 / TARGET_FPS)
    finally:
        close_canvas()


if __name__ == '__main__':
    main()
