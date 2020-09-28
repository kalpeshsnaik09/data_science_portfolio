import os
import time
import requests
import sys
import resource

def retrive_html():
    '''
        retrive climate data html file from url from year 2013 to 2018.
    '''
    for year in range(2013,2019):
        for month in range(1,13):
            try:
                if month<10:
                    url="https://en.tutiempo.net/climate/0{}-{}/ws-432950.html".format(month,year)
                else:
                    url="https://en.tutiempo.net/climate/{}-{}/ws-432950.html".format(month,year)
                texts=requests.get(url)
                text_utf=texts.text.encode("utf=8")
                if not os.path.exists("Data/html_data/{}".format(year)):
                    os.mkdir("Data/html_data/{}".format(year))
                with open("Data/html_data/{}/{}.html".format(year,month),"wb") as output:
                    output.write(text_utf)
            except Exception:
                continue
        sys.stdout.flush()

if __name__ == "__main__":
    start_time=time.time()
    retrive_html()
    stop_time=time.time()
    print("Process Time:{} Sec".format(round(stop_time-start_time,4)))
    MBytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
    print("Memory Used:{} MB".format(round(MBytes,4)))