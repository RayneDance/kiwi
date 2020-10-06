from django.db import models

class Recipes(models.Model):
 
	item_name = models.CharField(max_length=200)
	tier = models.IntegerField()
	type = models.CharField(max_length=200)
	mass = models.FloatField()
	volume = models.FloatField()
	outPutQuantity = models.IntegerField()
	time = models.IntegerField()
	byproducts =  models.ManyToManyField(Recipes)
	input = models.ManyToManyField('Input', through='Input')
	


class Input(models.Model):
	
	input = models.ForeignKey('Recipes')
	amount = models.FloatField()

