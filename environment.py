import random
import time


class DisasterEnvironment:
    def __init__(self):
        self.damage_levels = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
        self.current_damage = "LOW"

    def update_environment(self):
        self.current_damage = random.choice(self.damage_levels)

    def get_state(self):
        return {
            "damage_severity": self.current_damage,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }git