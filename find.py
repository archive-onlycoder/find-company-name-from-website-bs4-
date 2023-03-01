from bs4 import BeautifulSoup
import requests
import csv


def find_name(url):
    ok=False
    try:
        resp = requests.get('https://'+url,timeout=15)        
        if resp.status_code==200:
            ok=True
    except:
        pass
    
    if ok==False:
        try:
            resp = requests.get('http://'+url,timeout=15)    
            if resp.status_code==200:
                ok=True 
        except:
            pass

    
    if ok:
        soup=BeautifulSoup(resp.text,"lxml")
        try:
            dt=soup.find('title').text
            return dt
        except:
            return 'N/A'
    else:
        return 'N/A'
            

# print(find_name('creset.net'))

r=[]
file = open('import.csv')
csvreader = csv.reader(file)
c=0
for row in csvreader:
    name=find_name(row[0])
    if 'Account Suspended' in name:
        name='N/A'
    r=[row[0],name]
    f = open('export.csv', 'a')
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(r)
    print(c)
    c=c+1
    