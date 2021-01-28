import arcade
import random
import math

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
SCREEN_TITLE = "雷达"

RADAR_INIT = 0
RADAR_SEND = 1
RADAR_REFLEX = 2


class Target():
    def __init__(self):
       self.x, self.y = random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)

    def draw(self):
       math.draw_point(self.x, self.y, color.RED, 20)


class Wave():
    def __init__(self, send_angle):
        self.send_angle = send_angle
        self.send_x, self.send_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        self.send_r = 0

    def draw_send_wave(self):
        ox, oy = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        self.send_x, self.send_y = ox + self.send_r * math.sin(math.radians(self.send_angle)), oy + self.send_r * math.cos(math.radians(self.send_angle))
        math.draw_point(self.send_x, self.send_y, color.BLACK, 10)
        self.send_r += 3


class My_Radar(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()

    def setup(self):
        arcade.set_background_color(arcade.color.WHITE)
        self.angle = 0
        self.change_angle = 0
        self.status = RADAR_INIT
        self.Target = Target()
        self.Wave = Wave(self.angle)

    def on_draw(self):
        arcade.start_render()
        self.draw_radar()
        self.Target.draw()

    def on_update(self, delta_time):
        self.angle += self.change_angle

    def draw_radar(self):
        OX, OY = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        AX, AY = OX - 25, OY - 80
        BX, BY = OX, OY - 80
        CX, CY = OX + 25, OY - 80
        R = 50
        DX, DY = OX + R * \
            math.sin(math.radians(self.angle)), OY + R * \
            math.cos(math.radians(self.angle))

        draw_line(OX, OY, BX, BY, color.BLACK, 5)
        draw_line(AX, AY, CX, CY, color.BLACK, 5)
        math.draw_ellipse_filled(OX, OY, 100, 40, color.BLACK, 180 - self.angle)    
        if self.status == RADAR_SEND:
            self.Wave.draw_send_wave()
        draw_line(OX, OY, DX, DY, color.BLACK, 5)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.change_angle = -1
        elif symbol == key.RIGHT:
            self.change_angle = 1

    def on_key_release(self, symbol, modifiers):
        if symbol == key.SPACE and self.status == RADAR_INIT:
            self.status = RADAR_SEND
            self.Wave = Wave(self.angle)
        if symbol == key.LEFT or symbol == key.RIGHT:
            self.change_angle = 0


if __name__ == "__main__":
    game = My_Radar(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
