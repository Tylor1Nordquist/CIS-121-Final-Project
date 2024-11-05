'''
player = Player(attack=10, health=100, defence=5)

player.equip_weapon()
player.equip_armor()
'''


# To add, healing

class Player():
	def __init__(self, attack, health, defence):
		self.attack = attack
		self.health = health
		self.defence = defence
		self.hasWeapon = False
		self.hasArmor = False


# Runs while hasWeapon == False
	def equipWeapon(self):
		if not self.hasWeapon:
			self.attack *= 1.5
			self.hasWeapon = True      # Stops statement from running

# Runs while hasArmour == False
	def equipArmor(self):
		if not self.hasArmor:
			self.defence *= 1.1
			self.hasArmor = True  # Stops statement from running


# Charcter is attacking/dealing damage
	def isAttacking(self):
		return self.attack
	
# Charcter is defending/taking damage
	def isDefending(self, incoming_damage):
		#Returns health ensuring it does not pass zero
		self.health -= max(0, incoming_damage - self.defence)
		return self.health

	def isAlive(self):
		if self.health > 0:
			return True
		else:
			print (f'You died, better luck next time....')
			return False


# Overload Player function
	def __str__(self):
		stats_report = f'Player stats: Health {self.health}\nAttack {self.attack}\nDefence {self.defence}'
		return stats_report









# Example usage
player = Player(10, 100, 5)
print(player)  # Uses __str__ to display player stats
player.equipWeapon()
player.equipArmor()
print("Player attack after equipping weapon:", player.isAttacking())
print("Player health after taking 20 damage:", player.isDefending(20))
print("Is player alive?", player.isAlive())
