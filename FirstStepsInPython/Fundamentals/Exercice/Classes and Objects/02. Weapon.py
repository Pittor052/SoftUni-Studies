class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        if not self.bullets == 0:
            self.bullets -= 1
            result = "shooting..."
        else:
            result = "no bullets left"
        return result

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
