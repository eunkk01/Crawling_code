import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import schedule
import time
import pymysql
from sqlalchemy import create_engine
import datetime
import json

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


db_id = ''
db_pw = ''
db_name = ''


def nate_crawl():
    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    drv.get(f'https://news.nate.com/')

    bubbles = drv.find_element(By.CLASS_NAME, 'group-wrap.active').find_elements(By.CLASS_NAME, 'node')

    quarter = {'0': 1, '3': 2, '6': 3, '9': 4, '12': 5, '15': 6, '18': 7, '21': 8}
    hour = datetime.datetime.now().hour

    top_list = []
    for i in range(len(bubbles)):
        key_list = bubbles[i].find_element(By.CLASS_NAME, 'bubbleText').find_elements(By.CLASS_NAME, 'lineBreak')
        text = ''
        for j in range(len(key_list)):
            text += key_list[j].text
            text += ' '
        top_list.append(text.strip())

    rank = [i for i in range(1, 11)]
    top_keyword = pd.DataFrame(
        {'rank': rank, 'title': top_list, 'quarter': [f'q{str(quarter[str(hour)])}' for i in range(10)]})

    # user_nm = db_id
    # passwd = db_pw
    # host_url = host_url
    # port_num = num
    # db_name = db_name
    # engine = create_engine(f'mysql+pymysql://{user_nm}:{passwd}@{host_url}:{port_num}/{db_name}?charset=utf8mb4')
    # engine_conn = engine.connect()

    # insert
    # top_keyword.to_sql(upload_db_name, con=engine, if_exists='append', index=None)
    # engine_conn.close()
    # engine.dispose()


# 3시간마다 실시간 검색어 Top10 수집
schedule.every(3).hours.do(nate_crawl)

while True:
    schedule.run_pending()
    time.sleep(5)