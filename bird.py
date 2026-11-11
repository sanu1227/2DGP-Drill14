"""새 한 마리의 상태와 그리기."""

DRAW_WIDTH = 110
DRAW_HEIGHT = 101


class Bird:
    def __init__(self, image, x, y):
        self.image = image
        self.x = float(x)
        self.y = float(y)

    def draw(self):
        width = self.image.w // 5
        height = self.image.h // 3
        self.image.clip_draw(
            0, self.image.h - height, width, height,
            self.x, self.y, DRAW_WIDTH, DRAW_HEIGHT,
        )
