from django.db import models
from django.contrib import admin

class Recipes(models.Model):
 
	item_name = models.CharField(max_length=200)
	tier = models.IntegerField()
	type = models.CharField(max_length=200)
	mass = models.FloatField()
	volume = models.FloatField()
	outPutQuantity = models.IntegerField()
	time = models.IntegerField()
	byproducts =  models.ManyToManyField('Recipes')
	input = models.ManyToManyField('Recipes', through='Input', related_name="Required")

class Input(models.Model):

	required = models.ManyToManyField('Recipes', related_name="Subitem")
	amount = models.FloatField()

class Ore(models.Model):
	ore_name = models.ForeignKey('Recipes', on_delete=models.SET_NULL, null=True)
	ore_price = models.FloatField()

admin.site.register(Recipes)
admin.site.register(Ore)
