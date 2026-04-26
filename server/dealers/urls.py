from django.urls import path
from . import views

urlpatterns = [
    path('dealer/<int:dealer_id>/reviews/', views.get_dealer_reviews),
path('dealers/', views.get_all_dealers),
path('dealer/<int:dealer_id>/', views.get_dealer_by_id),
]