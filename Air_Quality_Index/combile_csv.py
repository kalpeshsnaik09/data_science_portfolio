from plot_extra_csv import avg_data
import pandas as pd 
import os
import sys
import requests
from bs4 import BeautifulSoup

def meta_data(year,month):
    file_html=open("Data/html_data/{}/{}.html".format(year,month),"rb")
    plain_text=file_html.read()

    final_data=[]

    soup=BeautifulSoup(plain_text,"lxml")
    for table in soup.findAll("table",{"class":"medias mensuales numspan"}):
        for tbody in table:
            temp=[]
            for tr in tbody:
                if tr.get_text()!='-':
                    temp.append(tr.get_text())
                else:
                    temp.append("")
            final_data.append(temp)
    
    final_data.pop(len(final_data)-1) # last row
    final_data.pop(len(final_data)-1) # second last row
    final_data.pop(0) # Column Header
    
    for i in final_data:
        i.pop(14) # FG Column
        i.pop(13) # TS Column
        i.pop(12) # SN Column
        i.pop(11) # RA Column
        i.pop(10) # VG Column
        i.pop(6) # PP Column
        i.pop(4) # SLP Column
        i.pop(0) # Day Column

    return final_data      


if __name__ == "__main__":
    final_dataset=[]
    for year in range(2013,2019):
        final_list=[]
        for month in range(1,13):
            final_list+=meta_data(year,month)
        df=pd.read_csv('Data/extra_csv_data/clean_aqi{}.csv'.format(year))
        for i in range(len(final_list)):
            try:
                final_list[i].append(list(df.iloc[:,1])[i])
            except:
                final_list[i].append("")
        final_dataset+=final_list
    data=pd.DataFrame(final_dataset)
    data.columns=['T', 'TM', 'Tm', 'H', 'VV', 'V', 'VM', 'PM2.5']
    data.to_csv("Data/main_data/air_quality_index.csv",index=False)
    data=pd.read_csv("Data/main_data/air_quality_index.csv")
    data.dropna(inplace=True)
    data=data.apply(pd.to_numeric)
    data.to_csv("Data/main_data/air_quality_index.csv",index=False)
    