#the website stop responding after 40ish requests
#the script obtains only the most popular GPUs
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import random 
from tqdm import tqdm
import json
headers={
        'User-Agent': 'Mozilla/5.0',
    }

#it scrapes only a small population (around 50) of most popular GPUs 
def scrape_gpu_popular():
    domain="https://www.techpowerup.com"
    url="https://www.techpowerup.com/gpu-specs/?sort=name"
    r=requests.get(url, headers=headers)
    soup=BeautifulSoup(r.text, 'html.parser')
    links={}
    links["NVIDIA"]=soup.select('td.vendor-NVIDIA > a')
    links["AMD"]=soup.select('td.vendor-AMD > a')
    links["Intel"]=soup.select('td.vendor-Intel > a')
    data_list=[]
    for vendor, links_ in links.items():
        print(f'------------------ {vendor}:{len(links_)} -----------------')
        for link in tqdm(links_):
            time.sleep(random.randint(1,10))
            href=link.get('href')
            r=requests.get(domain+href, headers=headers)
            soup=BeautifulSoup(r.text, 'html.parser')    
            name=soup.select('h1.gpudb-name')[0].getText()
            TDP=soup.select('dl:-soup-contains("TDP") > dd')[0].getText()
            print(f'name:{name}, vendor:{vendor}, TDP:{TDP}')
            data_list.append({'name':name, 'TDP':TDP, 'vendor':vendor})
            df=pd.DataFrame.from_dict(data_list)
            df.to_csv('gpu_popular.csv', index=False)

#it scrapes only a small population (around 50) of most popular CPUs 
def scrape_cpu_popular():
    url="https://www.techpowerup.com/cpu-specs/"
    r=requests.get(url, headers=headers)
    print(r.status_code)
    soup=BeautifulSoup(r.text, 'html.parser')
    rows=soup.select('table.processors > tr')
    data_list=[]
    for row in rows:
        cells=row.find_all('td')
        data_list.append({'name':cells[0].getText(), 'codename':cells[1].getText(), 'cores':cells[2].getText(), 'clock':cells[3].getText(), 'socket':cells[4].getText(), 'process':cells[5].getText(), 'L3 Cache':cells[6].getText(), 'TDP':cells[7].getText(), 'Released':cells[8].getText()})
    df=pd.DataFrame.from_dict(data_list)
    df.to_csv('cpu.csv', index=False)

#function for processing dump of all gpus obtained in scrape_gpu_all
def process_dump_gpu(path_dump, path_csv):
    with open(path_dump, 'r') as file:
        dump=json.load(file)
        data_list=[]
        for data in tqdm(dump):
            soup=BeautifulSoup(data['html'],'html.parser')
            rows=soup.select('table.processors > tr')
            tdp=data['TDP']
            if tdp == "unkown":
                pass
            for row in rows:
                cells=row.find_all('td')
                data_list.append({'name':cells[0].getText().strip(), 'gpu_chip':cells[1].getText().strip(), 'released':cells[2].getText().strip(), 'bus':cells[3].getText().strip(), 'memory':cells[4].getText().strip(), 'gpu_clock':cells[5].getText().strip(), 'memory_clock':cells[6].getText().strip(), 'shaders/TMUs/ROPs':cells[7].getText().strip(), 'TDP':tdp})
        df=pd.DataFrame.from_dict(data_list)
        df.to_csv(path_csv, index=False)

def scrape_gpu_all():
    url="https://www.techpowerup.com/gpu-specs/?sort=name"
    r=requests.get(url, headers=headers)
    soup=BeautifulSoup(r.text, 'html.parser')

    #Obtain all TDPs
    TDP_options=soup.select('select#tdp > option')
    TDP=[]
    #options:'All','unkown' are not considered
    for option in TDP_options[1:-1]:
        tdp=option.getText().split()[0]
        TDP.append(tdp)

    sleep_minutes=20
    dump=[]
    for tdp in tqdm(TDP):
        print(f'\nTDP:{tdp}\n')
        url=f"https://www.techpowerup.com/gpu-specs/?tdp={tdp}%20W&sort=name"
        r=requests.get(url, headers=headers)
        print(url)
        while r.status_code != 200:
            time.sleep(sleep_minutes*60)
            r=requests.get(url, headers=headers)
        dump.append({'TDP':tdp, 'html':r.text})
        with open('dump.json', 'w') as file:
            file.write(json.dumps(dump))
    process_dump_gpu('dump.json', 'gpu.csv')



#scrape_cpu_popular()
#scrape_gpu_popular()
#scarpe_gpu_all()