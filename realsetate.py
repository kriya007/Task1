import pandas as pd
import requests
import bs4 as BeautifulSoup
from bs4 import BeautifulSoup

url = "https://www.hkifa.org.hk/eng/associate-members.aspx"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

soup.findAll(attrs = {'class': 'first'})