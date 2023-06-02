from django.db import models


UNIT_CHOICES = (
	('kgs','kgs'),
	('grams','grams'),
	('mls','mls'),
	('pcs','pcs'),
	('portions','portions')
	)

class Meat(models.Model):
	
	meat = models.CharField(max_length = 20, unique = True)
	unit = models.CharField(max_length = 10, choices = UNIT_CHOICES, default = 'p')
	in_stock = models.IntegerField()
	reorder_level = models.IntegerField()
	status = models.CharField( max_length = 10, default	= 'UNKNOWN')

	def __str__(self):
		return self.meat

class Grocery(models.Model):
	
	grocery = models.CharField(max_length = 20, unique = True)
	unit = models.CharField(max_length = 10, choices = UNIT_CHOICES)
	in_stock = models.IntegerField()
	reorder_level = models.IntegerField()
	status = models.CharField( max_length = 10 )
	
	def __str__(self):
		return self.grocery

class Spice(models.Model):
	
	spice = models.CharField(max_length = 20, unique = True)
	unit = models.CharField(max_length = 10, choices = UNIT_CHOICES)
	in_stock = models.IntegerField()
	reorder_level = models.IntegerField()
	status = models.CharField( max_length = 10 )
	
	def __str__(self):
		return self.spice	

class Condiment(models.Model):
	
	condiment = models.CharField(max_length = 20, unique = True)
	unit = models.CharField(max_length = 10, choices = UNIT_CHOICES)
	in_stock = models.IntegerField()
	reorder_level = models.IntegerField()
	status = models.CharField( max_length = 10 )
	
	def __str__(self):
		return self.condiment

class Product(models.Model):
	
	product = models.CharField(max_length = 100, unique = True)
	unit = models.CharField(max_length = 10, choices = UNIT_CHOICES)
	in_stock = models.IntegerField()
	reorder_level = models.IntegerField()
	status = models.CharField( max_length = 10 )
	
	def __str__(self):
		return self.product		