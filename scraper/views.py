from django.shortcuts import render, redirect
from django.db import connections
from bs4 import BeautifulSoup
import requests
from contextlib import closing
import lxml
import csv
import copy
import os
from .models import Passing, Rushing, Kicking, Punting, Turnovers, Returning, Defense, Receiving

# Create your views here.

def passing(request):
  passing = Passing.objects.all()
  print(passing)
  return render(request, 'scraper/passing.html', {'passing': passing})

def rushing(request):
  rushing = Rushing.objects.all()
  print(rushing)
  return render(request, 'scraper/rushing.html', {'rushing': rushing})

def returning(request):
  returning = Returning.objects.all()
  print(returning)
  return render(request, 'scraper/returning.html', {'returning': returning})

def punting(request):
  punting = Punting.objects.all()
  print(punting)
  return render(request, 'scraper/punting.html', {'punting': punting})

def receiving(request):
  receiving = Receiving.objects.all()
  print(receiving)
  return render(request, 'scraper/receiving.html', {'receiving': receiving})

def turnovers(request):
  turnovers = Turnovers.objects.all()
  print(turnovers)
  return render(request, 'scraper/turnovers.html', {'turnovers': turnovers})

def defense(request):
  defense = Defense.objects.all()
  print(defense)
  return render(request, 'scraper/defense.html', {'defense': defense})

def scraper(request):
  var = ['passing', 'rushing', 'receiving', 'defense', 'kicking', 'punting', 'returning', 'givetake']

  for i in range(len(var)):

    url = f'http://www.espn.com/nfl/statistics/team/_/stat/{var[i]}'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}

    response = requests.get(url, headers = headers)

    # print(response.status_code)
    # print(url)
    # print(response.content)

    soup = BeautifulSoup(response.content, 'lxml')

    stat_table = soup.find_all('table', class_ = 'tablehead')

    # print(len(stat_table))
    # print(type(stat_table))

    stat_table = stat_table[0]
    # print(type(stat_table))

    # for row in stat_table.find_all('tr'):
    #   for cell in row.find_all('td'):
    #     print(cell.text)

    with open(f'{var[i]}_stats.csv', 'w') as r:
      for row in stat_table.find_all('tr'):
        for cell in row.find_all('td'):
          r.write(cell.text + ',') 
        r.write('\n')

  else:
    print('scraping complete')

  return redirect('/')

def import_csv(request):
  var = ['passing', 'rushing', 'receiving', 'defense', 'kicking', 'punting', 'returning', 'givetake']

  for i in range(len(var)):
    file = os.path.realpath(f'{var[i]}_stats.csv')

    with open(file, 'r') as csvfile:
      columns = csvfile.readline().split(',')
      columns.pop()
      table_name = f'{var[i]}'.title()

      with closing(connections['default'].cursor()) as cursor:
        cursor.copy_from(
          file=csvfile,
          table=table_name,
          sep=',',
          columns=(columns)
        ),

  print("Done!")

  return redirect('/')