import arcade

# Window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Player attributes
PLAYER_RADIUS = 25
PLAYER_SPEED = 5

class Bullet:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed

    def update(self):
        self.y -= self.speed

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)
        self.player_x = width // 2
        self.player_y = height // 2

        self.bullets = []
        self.bullet_radius = 5
        self.bullet_speed = 3
        self.bullet_cooldown = 60  # Number of frames between bullet spawns
        self.bullet_timer = 0

        # Enemy attributes
        self.enemy_x = width // 2
        self.enemy_y = height - PLAYER_RADIUS
        self.enemy_radius = 20

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.player_x, self.player_y, PLAYER_RADIUS, arcade.color.BLUE)
        arcade.draw_circle_filled(self.enemy_x, self.enemy_y, self.enemy_radius, arcade.color.RED)
        for bullet in self.bullets:
            arcade.draw_circle_filled(bullet.x, bullet.y, self.bullet_radius, arcade.color.BLACK)

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
        self.bullet_timer += 1
        if self.bullet_timer >= self.bullet_cooldown:
            self.bullets.append(Bullet(self.enemy_x, self.enemy_y - self.enemy_radius, self.bullet_radius, self.bullet_speed))
            self.bullet_timer = 0

        for bullet in self.bullets:
            bullet.update()

        if self.is_collision(self.player_x, self.player_y, self.enemy_x, self.enemy_y, PLAYER_RADIUS, self.enemy_radius):
            print("Game Over!")
    
    def is_collision(self, x1, y1, x2, y2, radius1, radius2):
        distance_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
        radius_sum_squared = (radius1 + radius2) ** 2
        return distance_squared <= radius_sum_squared

def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()
