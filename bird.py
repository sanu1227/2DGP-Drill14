"""새 한 마리의 상태와 그리기."""

from settings import CANVAS_WIDTH

DRAW_WIDTH = 110
DRAW_HEIGHT = 101
SHEET_COLUMNS = 5
SHEET_ROWS = 3
FRAME_COUNT = 14
FLAP_CYCLE_SECONDS = 0.7
ANIMATION_FPS = FRAME_COUNT / FLAP_CYCLE_SECONDS
LEFT_BOUND = DRAW_WIDTH / 2
RIGHT_BOUND = CANVAS_WIDTH - DRAW_WIDTH / 2
TRAVEL_SPAN = RIGHT_BOUND - LEFT_BOUND


class Bird:
    def __init__(self, image, x, y, speed=160.0, direction=1):
        self.image = image
        self.x = float(x)
        self.y = float(y)
        self.frame = 0.0
        self.speed = speed
        self.direction = direction
        # 오른쪽 진행은 왕복 경로의 전반부, 왼쪽 진행은 후반부에 놓는다.
        offset = self.x - LEFT_BOUND
        self.travel = offset if direction == 1 else 2 * TRAVEL_SPAN - offset

    def update(self, dt):
        self.travel = (self.travel + self.speed * dt) % (2 * TRAVEL_SPAN)
        if self.travel < TRAVEL_SPAN:
            self.x = LEFT_BOUND + self.travel
            self.direction = 1
        else:
            self.x = RIGHT_BOUND - (self.travel - TRAVEL_SPAN)
            self.direction = -1
        self.frame = (self.frame + ANIMATION_FPS * dt) % FRAME_COUNT

    def draw(self):
        row, column = divmod(int(self.frame), SHEET_COLUMNS)
        # 이미지가 격자 수로 나누어떨어지지 않으므로 각 셀 경계를 계산한다.
        left = column * self.image.w // SHEET_COLUMNS
        right = (column + 1) * self.image.w // SHEET_COLUMNS
        top = row * self.image.h // SHEET_ROWS
        bottom = (row + 1) * self.image.h // SHEET_ROWS
        # 이미지의 위쪽 기준 행을 pico2d의 아래쪽 기준 좌표로 바꾼다.
        self.image.clip_draw(
            left, self.image.h - bottom, right - left, bottom - top,
            self.x, self.y, DRAW_WIDTH, DRAW_HEIGHT,
        )
