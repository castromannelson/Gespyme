from django.urls import path
from apps.gespyme_products import views


# url endpoints for gespyme_products app

urlpatterns = [
    # Url for List data
    path('list', view=views.list_products.as_view(), name='Product_List'),
    # Url for Create data
    path('create', view=views.create_product.as_view(), name='Product_Create'),
    # Url for retrieve an especific registry by id 
    path('retrieve/<int:pk>/', view=views.retrieve_product.as_view(), name='Product_Retrienve_by_id'),
    # Url for update an especific registry by id
    path('update/<int:pk>/', view=views.update_product.as_view(), name='Product_Update_by_id'),
    # Url for destroy an especific registry by id
    path('destroy/<int:pk>', view=views.destoy_product.as_view(), name='Product_Destroy_by_id')
    
]
