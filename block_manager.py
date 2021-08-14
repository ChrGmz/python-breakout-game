from turtle import Turtle

COLOR_POINTS = {
    "red": 7,
    "orange": 5,
    "green": 3,
    "yellow": 1,
}


class BlockManager:
    def __init__(self):
        self.blocks = []
        self.set_blocks()

    def set_blocks(self):
        x_cor = -360
        y_cor = 180
        for color in COLOR_POINTS.keys():
            for _ in range(1, 3):
                for _ in range(1, 13):
                    self.create_new_block(color, (x_cor, y_cor))
                    x_cor += 65
                x_cor = -360
                y_cor -= 28

    def create_new_block(self, block_color, pos):
        new_block = Turtle("square")
        new_block.hideturtle()
        new_block.color(block_color)
        new_block.shapesize(stretch_wid=1, stretch_len=3)
        new_block.penup()
        new_block.goto(pos)
        new_block.showturtle()
        self.blocks.append(new_block)

    def has_hit(self, ball):
        for block in self.blocks:
            if block.distance(ball) < 30:
                self.blocks.remove(block)
                block.hideturtle()
                return COLOR_POINTS[block.pencolor()]
        return False

    def reset(self):
        for block in self.blocks:
            block.hideturtle()
            self.blocks.remove(block)
        self.set_blocks()
