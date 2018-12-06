from django.urls import path
from . import views

urlpatterns = [
  path('passing', views.passing, name='passing'),
  path('scraper', views.scraper, name='scraper'),
  path('import', views.import_csv, name='import'),
]