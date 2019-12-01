from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home, name='Home'), 
    path('contact/', views.about, name='Contact'), 
    path('details/<int:post_id>', views.post_details, name='details'), 
]