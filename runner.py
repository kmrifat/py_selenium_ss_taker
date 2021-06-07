import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import path

from pages.TakeSnapShot import TakeSnapShot

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options, executable_path='/home/rifat/chromedriver')

with open('demos_2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    ddddd = []
    for row in csv_reader:
        if not (path.exists(path.join(row[5], row[2].split(".")[0] + ".png"))):
            ddddd.append(row[2])
            # print('selenium will take ss')
            driver.get("http://" + row[2])
            snap = TakeSnapShot(driver)
            snap.take_snap(row[5], row[2])
        else:
            print('ss exists')
            print(driver.title)
        line_count += 1
    print(len(ddddd))
