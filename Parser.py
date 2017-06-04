import requests as rq
import calendar
from datetime import datetime
from bs4 import BeautifulSoup

print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
for year in range(2010, 2016):
    for month in range(1, 12):
        for date in range(1, calendar.monthrange(year, month)[1]):

            if(month<10):
                flag = str(year) + "-0" + str(month) + "-" + str(date)
            else:
                flag = str(year) + "-" + str(month) + "-" + str(date)

            url = "http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=466920&stname=%25E8%2587%25BA%25E5%258C%2597&datepicker=" + flag
            response = rq.get(url)
            html_doc = response.text
            soup = BeautifulSoup(response.text, "lxml")


            table = soup.find("table", {"id" : "MyTable"})

            record = ""
            for tr in table.findAll('tr', {"class" : ""}):
                for td in tr.findAll('td', {"nowrap": ""}):
                    text = td.find(text=True).replace(u'\xa0', u'')
                    if(text!=''):
                        record = record + text + ','
                record = record + ';'

            record = record[:-2]
            #print(record)
            list = record.split(",;")

            with open('history.txt', mode='a', encoding='utf-8') as myfile:
                myfile.write('\n'.join(list))
                myfile.write('\n')
            myfile.close
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))