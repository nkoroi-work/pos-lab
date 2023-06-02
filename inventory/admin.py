from django.contrib import admin
from django.apps import apps

inventory_models = apps.get_app_config('inventory').get_models()
for m in inventory_models:
	admin.site.register(m)
