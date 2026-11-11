"""10마리 새의 생성과 일괄 갱신."""

from pico2d import load_image

from bird import Bird
from settings import BIRD_COUNT


class Flock:
    def __init__(self):
        # 같은 텍스처를 10마리가 공유하며 각 새의 상태는 독립적으로 보관한다.
        self.image = load_image('bird_animation.png')
        self.birds = [
            Bird(self.image, 250 + (i // 5) * 600, 90 + (i % 5) * 130)
            for i in range(BIRD_COUNT)
        ]

    def update(self, dt):
        for bird in self.birds:
            bird.update(dt)

    def draw(self):
        for bird in self.birds:
            bird.draw()
