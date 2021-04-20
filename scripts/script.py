from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json

url = "https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield"
def treasury_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    table = soup.find("table", attrs= {"class":"t-chart"})
    rows = table.find_all('tr')
    th_td_list = []
    
    for row in rows[1:]:
        tds = row.findAll('td')
        th_td_data_row = []
        for td in tds:
            td_text = td.text.strip()
            if '.' in td_text:
                count_digits = len(td_text) - td_text.index('.')- 1
                td_text = int(''.join(td_text.split('.'))) / 10 ** count_digits
            th_td_data_row.append(td_text)
        th_td_list.append(th_td_data_row)
        print(th_td_list)
    return th_td_list

treasury_data(url)