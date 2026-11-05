# Activity 5 - Understanding Polymorphism
# Written answers based on Activities 2, 3, and 4 in Study Guide 11.

# 1. What do all the methods (move(), special_move(), use()) in the previous
#    activities have in common?
#
# Answer:
# They have the same method names within their respective classes but perform
# different actions depending on the object calling them. This demonstrates
# polymorphism.

# 2. How does this activity show polymorphism in a gaming context?
#
# Answer:
# It shows polymorphism because different game characters and items can use
# the same method name but produce different behaviors. For example, different
# characters perform different special moves, while different potions produce
# different effects.

# 3. Can you think of other examples where the same action behaves differently
#    depending on the character or item?
#
# Answer:
# Yes. A method called attack() could make a Warrior perform a sword attack,
# a Mage cast a magic spell, and an Archer shoot an arrow. Similarly, a method
# called equip() could allow different weapons or armor to equip themselves
# differently.