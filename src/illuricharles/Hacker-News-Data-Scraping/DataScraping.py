
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd 
import os


def check_request(url):

  # Sending request
  req = requests.get(url, timeout=10)
  time.sleep(2)
  print(f'[+] Request sent to {url}')

  # Checking the status code of the web page
  if req.status_code != 200:
    raise Exception(f'failed to load web page {url} {req.status_code}')
  return req.text

def get_content(doc):

  # Collecting information about required tag
  title_content = doc.find_all('span', {'class': 'titleline'})
  score_content = doc.find_all('span', {'class': 'score'})
  return title_content, score_content



def get_information(title_content, score_content, score, data):

  titles = [title.text for title in title_content]
  scores = [int(cur_score.text.replace('points','')) for cur_score in score_content]
  title_content[0].a['href']
  links = [link.a['href'] for link in title_content]

  # Checking the score 
  for idx, cur_score in enumerate(scores):
    if cur_score >= score:
      data['titles'].append(titles[idx])
      data['scores'].append(scores[idx])
      data['links'].append(links[idx])
  return data


def scrap_data(url, page_no, score):

  # Checking valid input
  if page_no < 1 or page_no > 30:
    raise Exception(f'Page number is not in required range(1-30)')
  print("please wait, It takes sometime to complete because to avoid overload on server.......")
  if score <1:
    raise Exception(f'Score value should be positive: ')


  # Creating dictionary to store values
  data = {
      'titles': [],
      'scores': [],
      'links': []
  }

  
  # Scraping each page
  for i in range(1,page_no+1):
    req_url = url + str(i)
    req_txt = check_request(req_url)
    doc = BeautifulSoup(req_txt, 'html.parser')
    title_content, score_content = get_content(doc)
    data = get_information(title_content, score_content, score, data)
  create_csv(data)


def create_csv(information):

  print('[+] Creating New Data Folder To Store Data')
  time.sleep(1)

  # Creating new folder
  os.makedirs('data', exist_ok = True)
  fname = 'data/'+'information.xlsx'  
  information_df = pd.DataFrame(information)
  print(f'[+] New information.xlsx File Created To Store Scraped Data')
  time.sleep(1)
  store_status = 'yes'
  # checking if file exist
  if os.path.exists(fname):
    store_status = check_exists_data()
  if store_status == 'yes':
    print('[+] Storing Data')
    information_df.to_excel(fname)
    print(f'[+] Execution Completed')
  else:
    print(f'[-] Execution stopped.')


# Function which return the status to override data or not
def check_exists_data():
  print('[-] information.xlsx file already exists in data folder')
  time.sleep(1)
  print('[?] Do You Want To Override Data in information.xlsx folder (Yes/No)')
  status = input()
  status = status.lower()
  while(status != 'yes' and status!= 'no'):
    print('[-] Input is not correct format')
    print('[?] Do You Want To Override Data in information.xlsx folder (Yes/No)')
    status = input()
    status = status.lower()
  return status

if __name__ == "__main__":
  url = 'https://news.ycombinator.com/news?p='
  page_no = int(input('No of Pages you want to scrap, range(1-30): '))
  score = int(input('Enter minimun point value [Example -> 100]: '))
  scrap_data(url, page_no, score)

