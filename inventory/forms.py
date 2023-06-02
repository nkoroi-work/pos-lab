from django import forms
from .models import *

class MeatForm(forms.ModelForm):
		class Meta:
			model = Meat
			fields = "__all__"

class GroceryForm(forms.ModelForm):
		class Meta:
			model = Grocery
			fields = "__all__"

class SpiceForm(forms.ModelForm):
		class Meta:
			model = Spice
			fields = "__all__"

class CondimentForm(forms.ModelForm):
		class Meta:
			model = Condiment
			fields = "__all__"

class ProductForm(forms.ModelForm):
		class Meta:
			model = Product
			fields = "__all__"