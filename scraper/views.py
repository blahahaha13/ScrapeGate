from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import lxml
import requests
import csv


# Create your views here.

def results(request):
  return render(request, 'scraper/results.html')

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

    with open (f'{var[i]}_stats.csv', 'w') as r:
      for row in stat_table.find_all('tr'):
        for cell in row.find_all('td'):
          r.write(cell.text + ',') 
        r.write('\n')

  else:
    print('scraping complete')

  return redirect('/scraper/results')