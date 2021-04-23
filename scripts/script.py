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

def chart():
    data = treasury_data(url)
    df = pd.DataFrame(data, columns= ["Date", "1Mo", "2Mo", "3Mo", "6Mo", "1Yr","2Yr","3Yr","5Yr","7Yr", "10Yr", "20Yr", "30Yr"])
    labels = ["1Yr","2Yr","3Yr","5Yr","7Yr", "10Yr", "20Yr", "30Yr"]
    fig,ax = plt.subplots(figsize= (20,10))
    ax.plot(df.groupby("Date")[["1Yr","2Yr","3Yr","5Yr","7Yr", "10Yr", "20Yr", "30Yr"]].sum())
    ax.set(title= "Treasury data in the last 30 years",ylabel ="Yield Curve Rates", xlabel ="Dates")
    ax.legend(labels)
    plt.savefig('../charts/Dailyycr.png')

def main():
    data = treasury_data(url)
    chart()

if __name__ == '__main__':
    main()