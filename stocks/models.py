from django.db import models
from orders.models import Tab
from inventory.models import *


DISH_CHOICES = {}
BEER_CHOICES = {}
SIDE_CHOICES = {}
SNACK_CHOICES = {}
CARBONATED_DRINK_CHOICES = {}
LIQUOR_CHOICES = {}
JUICE_CHOICES = {}
WINE_CHOICES = {}
WATER_CHOICES = {}


class Dish(models.Model):
	
	dish = models.CharField(max_length = 20, choices = DISH_CHOICES)
	quantity = models.IntegerField()
	tab = models.ForeignKey(Tab, on_delete = models.CASCADE)
	
	def __str__(self):
		return self.dish

class Side(models.Model):
	
	side = models.CharField(max_length = 20, choices = SIDE_CHOICES)
	quantity = models.IntegerField()
	tab = models.ForeignKey(Tab, on_delete = models.CASCADE)
	def __str__(self):
		return self.side

class Snack(models.Model):
	
	snack = models.CharField(max_length = 20, choices = SNACK_CHOICES)
	quantity = models.IntegerField()
	tab = models.ForeignKey(Tab, on_delete = models.CASCADE)
	def __str__(self):
		return self.snack

class CarbonatedDrink(models.Model):
	
	carbonated_drink = models.CharField(max_length = 20, choices = CARBONATED_DRINK_CHOICES)
	quantity = models.IntegerField()
	tab = models.ForeignKey(Tab, on_delete = models.CASCADE)
	def __str__(self):
		return self.carbonated_drink


class Beer(models.Model):
	
	beer = models.CharField(max_length = 20, choices = BEER_CHOICES)
	quantity = models.IntegerField()
	tab = models.ForeignKey(Tab, on_delete = models.CASCADE)
	def __str__(self):
		return self.beer

class Liquor(models.Model):
	
	liquor = models.CharField(max_length = 20, choices = LIQUOR_CHOICES)
	quantity = models.IntegerField()
	tab = models.ForeignKey(Tab, on_delete = models.CASCADE)
	def __str__(self):
		return self.liquor

class Juice(models.Model):
	
	juice = models.CharField(max_length = 20, choices = JUICE_CHOICES)
	quantity = models.IntegerField()
	tab = models.ForeignKey(Tab, on_delete = models.CASCADE)
	def __str__(self):
		return self.juice

class Wine(models.Model):
	
	wine = models.CharField(max_length = 20, choices = WINE_CHOICES)
	quantity = models.IntegerField()
	tab = models.ForeignKey(Tab, on_delete = models.CASCADE)
	def __str__(self):
		return self.wine

class Water(models.Model):
	
	water = models.CharField(max_length = 20, choices = WATER_CHOICES)
	quantity = models.IntegerField()
	tab = models.ForeignKey(Tab, on_delete = models.CASCADE)
	def __str__(self):
		return self.water

class SwimmingPassA(models.Model):
	
	quantity = models.IntegerField()
	tab = models.ForeignKey(Tab, on_delete = models.CASCADE)
	def __str__(self):
		return self.swimmin_pass_a

class SwimmingPassS(models.Model):
	
	quantity = models.IntegerField()
	tab = models.ForeignKey(Tab, on_delete = models.CASCADE)
	def __str__(self):
		return self.swimming_pass_s

class SwimmingPassC(models.Model):
	
	quantity = models.IntegerField()
	tab = models.ForeignKey(Tab, on_delete = models.CASCADE)
	def __str__(self):
		return self.swimming_pass_c

class SwimmingPassR(models.Model):
	
	quantity = models.IntegerField()
	tab = models.ForeignKey(Tab, on_delete = models.CASCADE)
	def __str__(self):
		return self.swimming_pass_r

class RoomA(models.Model):
	
	quantity = models.IntegerField()
	tab = models.ForeignKey(Tab, on_delete = models.CASCADE)
	def __str__(self):
		return self.room_a

class RoomB(models.Model):
	
	
	quantity = models.IntegerField()
	tab = models.ForeignKey(Tab, on_delete = models.CASCADE)
	def __str__(self):
		return self.room_b

class RoomC(models.Model):
	
	quantity = models.IntegerField()
	tab = models.ForeignKey(Tab, on_delete = models.CASCADE)
	def __str__(self):
		return self.room_c

class RoomD(models.Model):
	
	quantity = models.IntegerField()
	tab = models.ForeignKey(Tab, on_delete = models.CASCADE)
	def __str__(self):
		return self.room_d

class Tent(models.Model):

	quantity = models.IntegerField()
	tab = models.ForeignKey(Tab, on_delete = models.CASCADE)
	def __str__(self):
		return self.tent