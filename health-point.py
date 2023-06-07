import arcade

# Window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Player attributes
PLAYER_RADIUS = 25
PLAYER_SPEED = 5

# Enemy attributes
ENEMY_RADIUS = 20
ENEMY_HEALTH = 100

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)
        self.player_x = width // 2
        self.player_y = height // 2

        self.enemy_x = width // 2
        self.enemy_y = height - PLAYER_RADIUS
        self.enemy_health = ENEMY_HEALTH

        print(self.enemy_health)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.player_x, 
                                  self.player_y, 
                                  PLAYER_RADIUS, 
                                  arcade.color.BLUE)
        if self.enemy_health > 0:
            arcade.draw_circle_filled(self.enemy_x, 
                                      self.enemy_y, 
                                      ENEMY_RADIUS, 
                                      arcade.color.RED)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_x -= PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player_x += PLAYER_SPEED
        elif key == arcade.key.UP:
            self.player_y += PLAYER_SPEED
        elif key == arcade.key.DOWN:
            self.player_y -= PLAYER_SPEED

    def update(self, delta_time):
        if self.is_collision(self.player_x, self.player_y, 
                             self.enemy_x, self.enemy_y, 
                             PLAYER_RADIUS, ENEMY_RADIUS):
            self.enemy_health -= 10
            print(self.enemy_health)

    def is_collision(self, x1, y1, x2, y2, radius1, radius2):
        distance_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
        radius_sum_squared = (radius1 + radius2) ** 2
        return distance_squared <= radius_sum_squared

def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()
