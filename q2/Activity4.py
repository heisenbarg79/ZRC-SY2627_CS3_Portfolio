# Activity 4 - Game Character Potion Use
# Demonstrates duck typing using a shared use() method.
# Note: The study guide's item.user() is a typo; the method is item.use().

class HealthPotion:
    def use(self):
        print("You regain 50 HP!")


class ManaPotion:
    def use(self):
        print("You restore 30 MP!")


class SpeedBoost:
    def use(self):
        print("Your speed increases for 10 seconds!")


def apply_item(item):
    item.use()


health_potion = HealthPotion()
mana_potion = ManaPotion()
speed_boost = SpeedBoost()

potions = [health_potion, mana_potion, speed_boost]

for potion in potions:
    apply_item(potion)
