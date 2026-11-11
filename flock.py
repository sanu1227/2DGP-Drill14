"""10마리 새의 생성과 일괄 갱신."""

from random import Random

from pico2d import load_image

from bird import Bird, FRAME_COUNT
from settings import BIRD_COUNT


class Flock:
    def __init__(self):
        # 같은 텍스처를 10마리가 공유하며 각 새의 상태는 독립적으로 보관한다.
        self.image = load_image('bird_animation.png')
        # 고정 시드로 다시 실행해도 같은 초기 새떼를 볼 수 있다.
        random = Random(14)
        self.birds = [
            Bird(
                self.image,
                x=250 + (i // 5) * 600 + random.uniform(-70, 70),
                y=90 + (i % 5) * 130 + (i // 5) * 35,
                speed=random.uniform(120, 200),
                direction=1 if i % 2 == 0 else -1,
                frame=random.uniform(0, FRAME_COUNT),
            )
            for i in range(BIRD_COUNT)
        ]

    def update(self, dt):
        for bird in self.birds:
            bird.update(dt)

    def draw(self):
        for bird in self.birds:
            bird.draw()
