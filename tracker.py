import requests
from bs4 import BeautifulSoup
import difflib
import time
from datetime import datetime

url = "https://www.facebook.com/"
headers = {"User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

pv = ""
fr = True
while True:

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    for script in soup(["script", "style"]):
        script.extract() 
    soup = soup.get_text()
    if pv != soup:
        if fr == True:
            pv = soup
            fr = False
            print ("Start Monitoring "+url+ ""+ str(datetime.now()))
        else:
            print ("Changes detected at: "+ str(datetime.now()))
            OldPage = pr.splitlines()
            NewPage = soup.splitlines()
            d = difflib.Differ()
            diff = d.compare(OldPage, NewPage)
            out_text = "\n".join([ll.rstrip() for ll in '\n'.join(diff).splitlines() if ll.strip()])
            print (out_text)
            OldPage = NewPage
    
            pv = soup
    else:
        print( "No Changes "+ str(datetime.now()))
    time.sleep(10)
    continue