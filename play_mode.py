"""기존 소년/잔디 장면과 새떼를 같은 프레임 시간으로 갱신한다."""

from pico2d import (
    SDL_KEYDOWN, SDL_QUIT, SDLK_ESCAPE,
    clear_canvas, get_events, update_canvas,
)

import game_framework
import game_world
from ball import Ball
from boy import Boy
from flock import Flock
from grass import Grass

boy = None
flock = None


def init():
    global boy, flock
    game_world.add_oject(Grass(), 0)
    boy = Boy()
    game_world.add_oject(boy)
    flock = Flock()


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT or (
            event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
        ):
            game_framework.quit()
            return
        boy.handle_event(event)


def update():
    game_world.update()
    flock.update(game_framework.frame_time)


def render():
    clear_canvas()
    game_world.render()
    flock.draw()
    update_canvas()


def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy, flock
    game_world.clear()
    boy = None
    flock = None
    Ball.images.clear()
