from django.urls import path
from . import views

urlpatterns = [
  path('results', views.results, name='results'),
  path('scraper', views.scraper, name='scraper'),
]