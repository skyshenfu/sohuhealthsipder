# coding=utf-8
import unittest
from  selenium import webdriver
from bs4 import BeautifulSoup
import time
import codecs

import csv

from selenium.common.exceptions import NoSuchElementException


class selTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()

    def testEle(self):
        driver = self.driver
        driver.get("http://sj.qq.com/myapp/search.htm?kw=%E8%B5%84%E6%9C%AC")
        for i in range(50):
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
           # if driver.find_element_by_link_text(u'没有更多了').
            if (len(driver.find_elements_by_link_text(u'加载更多'))!=0):
                driver.find_element_by_link_text(u'加载更多').click()
                print i
                continue
            time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        alist = soup.find_all("a", {"class": "installBtn"})
        # print "http:"+div.a['href']
        # print div.a.string
        with open('./data/关键字资本.csv', 'w') as csvfile:
            csvfile.write(codecs.BOM_UTF8)
            fieldnames = ['name', 'icon','url','redirecturl','package']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for a in alist:
                print a
                name = a['appname'].encode("utf-8")
                icon=a['appicon']
                package=a['apk']
                url="http://sj.qq.com/myapp/detail.htm?apkName="+package
                redirecturl=a['ex_url'].encode("utf-8")
                writer.writerow({'name': name,'icon':icon,'package':package,'url':url,'redirecturl':redirecturl})

    def tearDown(self):
        print ''


if __name__ == "__main__":
    unittest.main()
