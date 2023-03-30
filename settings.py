class Settings:

    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)

        # Bullets settings
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullet_speed=2.0
        self.allowed_bullets=5

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represent left
        self.fleet_direction = 1

        # Ship settings
        self.ship_speed = 1.2
        self.ship_limit = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale=1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 1.2
        self.bullet_speed = 2.0
        self.alien_speed = 1.0
        # Scoring
        self.alien_points=20
        self.max_alien_points=self.alien_points

        # Fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points=int(self.alien_points * self.score_scale)
