# Hacker-News-Data-Scraping

Hacker News is a social news website focusing on computer science and entrepreneurship. It contains some useful information. With the help of data scraping we can process the data of the web pages quickly and store the data.
Data scraping is the process of extracting and parsing data from websites in an automated fashion using a computer program. It's a useful technique for creating datasets for research and learning. It is developed using python3.
 

### Required Libraries
- Requests
- BeautifulSoup
- Pandas


### First clone the repo
```
git clone https://github.com/theadeyemiolayinka/python-scripts.git
```

### Move into the directory
```
cd python-scripts/src/illuricharles/Hacker-News-Data-Scraping
```

### Install Requirements
```
pip install -r requirements.txt
```
### Execute the program
```
python DataScraping.py
```

### Steps
- First enter the number of pages that you want to scrape, page range is from 1-30
- Enter the minimum score value. Example if you enter 100, data which have 100 or more than 100 points will be collected.
- It will create a new folder 'data' where the DataScraping.py code is persent.
- In that data folder the collected data will store in excel format.
- **Note** that if the excel sheet already pesent it will ask "Do You Want To Override Data". If you enter yes then the excel sheet will add new data and remove previous data.



