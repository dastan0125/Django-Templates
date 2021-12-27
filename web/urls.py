from django.urls import path

from . import views
from .views import ProductDetailsView

urlpatterns = [
    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
]