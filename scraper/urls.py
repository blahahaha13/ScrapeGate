from django.urls import path
from . import views

urlpatterns = [
  path('passing', views.passing, name='passing'),
  path('receiving', views.receiving, name='receiving'),
  path('returning', views.returning, name='returning'),
  path('defense', views.defense, name='defense'),
  path('punting', views.punting, name='punting'),
  path('rushing', views.rushing, name='rushing'),
  path('turnovers', views.turnovers, name='turnovers'),
  path('scraper', views.scraper, name='scraper'),
  path('import', views.import_csv, name='import'),
]