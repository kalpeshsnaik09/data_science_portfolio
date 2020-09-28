import pandas as pd
import matplotlib.pyplot as plt 
import os

def avg_data(path):
    average=[]
    for rows in pd.read_csv(path,chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var+=temp
        avg=add_var/24
        average.append(avg)
    return average

if __name__ == "__main__":
    dir_path="Data/extra_csv_data"
    for path in os.listdir(dir_path):
        full_path=os.path.join(dir_path,path)
        new_path=os.path.join(dir_path,'clean_'+path)
        if os.path.isfile(full_path):
            pd.DataFrame(avg_data(full_path)).to_csv(new_path)
            