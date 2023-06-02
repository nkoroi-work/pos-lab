from django.urls import path
from .views import *
from .forms import *

urlpatterns = [
    path('<str:model_name>/<int:pk>/', universal_detail_view, name='universal_detail'),
    path('<str:model_name>/<int:pk>/update/', universal_update_view, name='universal_update'),
    path('<str:model_name>/<int:pk>/delete/', universal_delete_view, name='universal_delete'),

    path('create/meat',universal_create_view,{'form_class': MeatForm}, name='name_create'),
    path('create/grocery',universal_create_view,{'form_class': GroceryForm}, name='grocery_create'),
    path('create/spice',universal_create_view,{'form_class': SpiceForm}, name='spice_create'),
    path('create/condiment',universal_create_view,{'form_class': CondimentForm}, name='condiment_create'),
    path('create/product',universal_create_view,{'form_class': ProductForm}, name='product_create'),

    
    path('list/', list_view, name='list'),

]