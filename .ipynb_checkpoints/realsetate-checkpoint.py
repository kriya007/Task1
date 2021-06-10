import pandas as pd
import requests
import bs4 as BeautifulSoup

url = "https://www.hkifa.org.hk/eng/associate-members.aspx"

page = requests.get(url)
page.content