import os
import requests
from bs4 import BeautifulSoup
from exporter import save_to_file
os.system("clear")
alba_url = "http://www.alba.co.kr"

def extract_job_link():
  try:
    r = requests.get(alba_url)
    bs = BeautifulSoup(r.text,"html.parser")
    jobs = bs.find("div",{"id":"MainSuperBrand"}).find_all("li",{"class":"impact"})
    job_links = []
    for job in jobs:
      name = job.find("span",{"class":"company"}).text
      link = job.find("a",{"class":"goodsBox-info"})['href']
      job_links.append({"name":name,"link":link})
  except:
    print(f"{alba_url} is Down")
  return job_links

job_links = extract_job_link()
for i in range(0,len(job_links)):
  try:
    print(f"[Scrapping] {job_links[i]['link']}")
    r = requests.get(job_links[i]['link'])
    bs = BeautifulSoup(r.text,"html.parser")
    job_list = bs.find("tbody").find_all("tr",{"class":""})
    jobs=[]
    for job in job_list:
      place = job.find("td",{"class":"local"}).text
      title = job.find("span",{"class":"title"}).text
      time = job.find("span",{"class":"time"}).text
      pay = job.find("td",{"class":"pay"}).text
      date = job.find("td",{"class":"regDate"}).text
      link = job.find("td",{"class":"title"}).find("a")['href']
      jobs.append({"place":place,"title":title,"time":time,"pay":pay,"date":date,"link":link})
    save_to_file(job_links[i]['name'],jobs)
  except:
    print(f"{job_links[i]['link']} have 0 Jobs")
print("[Scrapping Done]")
 



