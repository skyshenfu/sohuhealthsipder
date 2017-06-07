# coding=utf-8
import unittest
from  selenium import webdriver
from bs4 import BeautifulSoup
import time
import codecs

import csv


class selTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()

    def testEle(self):
        driver = self.driver
        driver.get("http://health.sohu.com/")
        for i in range(100):
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        divs = soup.find_all("div", {"data-role": "news-item"})
        # print "http:"+div.a['href']
        # print div.a.string
        with open('./data/result.csv', 'w') as csvfile:
            csvfile.write(codecs.BOM_UTF8)
            fieldnames = ['title', 'srcurl']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for div in divs:
                strtitle = div.h4.a.string.strip().encode("utf-8")
                strurl = "http:" + div.h4.a['href']
                writer.writerow({'title': strtitle, 'srcurl': strurl})

    def tearDown(self):
        print ''


if __name__ == "__main__":
    unittest.main()
