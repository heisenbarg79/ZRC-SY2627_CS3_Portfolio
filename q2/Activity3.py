# Activity 3 - Game Character Special Moves
# Demonstrates duck typing using a shared special_move() method.

class Warrior:
    def special_move(self):
        print("Warrior swings a mighty sword!")


class Mage:
    def special_move(self):
        print("Mage casts a powerful spell!")


class Archer:
    def special_move(self):
        print("Archer shoots a precise arrow!")


def perform_move(character):
    character.special_move()


warrior = Warrior()
mage = Mage()
archer = Archer()

characters = [warrior, mage, archer]

for character in characters:
    perform_move(character)
