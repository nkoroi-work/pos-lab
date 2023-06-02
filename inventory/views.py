from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import *
from . import forms
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist

STATUS_CHOICES = {0: 'OUT OF STOCK', 1:'OVER-STOCKED',2:'GOOD',3:'REORDER',4:'LOW'}

inventory_models = apps.get_app_config('inventory').get_models()


#FUNCTIONS

def check_status(M):
	if M.in_stock >= 4 * M.reorder_level:
		return 1
	elif M.in_stock > 2 * M.reorder_level and M.in_stock <= 4 * M.reorder_level:
		return 2
	elif M.in_stock == M.reorder_level:
		return 3
	elif M.in_stock < M.reorder_level and M.in_stock> 0:
		return 4
	elif M.in_stock == 0:
		return 0

def set_status(models):
	for M in models:
		status = check_status(M)
		M.status = STATUS_CHOICES.get(status, 'UNKNOWN')
		M.save()
#views

def universal_create_view(request, form_class):
	if request.method == 'POST':
		form = form_class(request.POST)
		if form.is_valid():
			form.save()
			return redirect('success_url')
	else:
		form = form_class()
	return render(request, 'inventory/create_view.html', {'form': form})

def universal_update_view(request, model_name, pk):
	model = globals()[model_name]
	form_class = globals()[f'{model_name}Form']
	obj = get_object_or_404(model, pk=pk)
	if request.method == 'POST':
		form = form_class(request.POST, instance=obj)
		if form.is_valid():
			form.save()
			return redirect(reverse('inventory : universal_detail_view	', args=[model_name, pk]))
	else:
		form = form_class(instance=obj)
	context = {'form': form}
	return render(request, 'inventory/update.html', context)

def universal_delete_view(request, model_name, pk):
	model = globals()[model_name]
	obj = get_object_or_404(model, pk=pk)
	if request.method == 'POST':
		obj.delete()
		return redirect(reverse('inventory:list'))
	context = {'object': obj}
	return render(request, 'inventory/delete.html', context)

def universal_detail_view(request, model_name, pk):
	model = globals()[model_name]
	obj = get_object_or_404(model, pk=pk)
	context = {'object': obj}
	return render(request, 'inventory/detail_view.html', context)

#list

def list_view(request):
	context = {}

	meat_model_instances = Meat.objects.all()
	context.update({'meat_model_instances': meat_model_instances})
	try:
		set_status(meat_model_instances)
	except ObjectDoesNotExist:
		pass

	try:
		value = meat_model_instances[0]
		meat_index_error = False
	except IndexError:
		meat_index_error = True

	context.update({'meat_index_error': meat_index_error})

	grocery_model_instances = Grocery.objects.all()
	context.update({'grocery_model_instances': grocery_model_instances})
	try:
		set_status(grocery_model_instances)
	except ObjectDoesNotExist:
		pass

	try:
		value = grocery_model_instances[0]
		grocery_index_error = False
	except IndexError:
		grocery_index_error = True

	context.update({'grocery_index_error': grocery_index_error})


	spice_model_instances = Spice.objects.all()
	context.update({'spice_model_instances': spice_model_instances})
	try:
		set_status(spice_model_instances)
	except ObjectDoesNotExist:
		pass

	try:
		value = spice_model_instances[0]
		spice_index_error = False
	except IndexError:
		spice_index_error = True

	context.update({'spice_index_error': spice_index_error})


	condiment_model_instances = Condiment.objects.all()
	context.update({'condiment_model_instances': condiment_model_instances})
	try:
		set_status(condiment_model_instances)
	except ObjectDoesNotExist:
		pass

	try:
		value = condiment_model_instances[0]
		condiment_index_error = False
	except IndexError:
		condiment_index_error = True

	context.update({'condiment_index_error': condiment_index_error})



	product_model_instances = Product.objects.all()
	context.update({'product_model_instances': product_model_instances})
	try:
		set_status(product_model_instances)
	except ObjectDoesNotExist:
		pass

	try:
		value = product_model_instances[0]
		product_index_error = False
	except IndexError:
		product_index_error = True

	context.update({'product_index_error': product_index_error})

	return render(request, "inventory/list_view.html", context)

#create

def meat_create_view(request):
	return universal_create_view(request, MeatForm)

def grocery_create_view(request):
	return universal_create_view(request, GroceryForm)

def spice_create_view(request):
	return universal_create_view(request, SpiceForm)

def condiment_create_view(request):
	return universal_create_view(request, CondimentForm)

def product_create_view(request):
	return universal_create_view(request, ProductForm)
#update

def meat_update_view(request, pk):
	universal_update_view('Meat', pk)

def grocery_update_view(request, pk):
	universal_update_view('Grocery', pk)

def spice_update_view(request, pk):
	universal_update_view('Spice', pk)

def condiment_update_view(request, pk):
	universal_update_view('Condiment', pk)

def product_update_view(request, pk):
	universal_update_view('Product', pk)

#delete

def meat_delete_view(request, pk):
	universal_delete_view('Meat', pk)

def grocery_delete_view(request, pk):
	universal_delete_view('Grocery', pk)

def spice_delete_view(request, pk):
	universal_delete_view('Spice', pk)

def condiment_delete_view(request, pk):
	universal_delete_view('Condiment', pk)

def product_delete_view(request, pk):
	universal_delete_view('Product', pk)

#detail

def meat_detail_view(request, pk):
	universal_detail_view('Meat', pk)

def grocery_detail_view(request, pk):
	universal_detail_view('Grocery', pk)

def spice_detail_view(request, pk):
	universal_detail_view('Spice', pk)

def condiment_detail_view(request, pk):
	universal_detail_view('Condiment', pk)

def product_detail_view(request, pk):
	universal_detail_view('Product', pk)

