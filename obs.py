# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giris.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = False
browser = webdriver.Firefox(options=options, executable_path=r'geckodriver.exe')
browser.implicitly_wait(10)

url = 'https://ogr.kocaeli.edu.tr/koubs/ogrenci/index.cfm'
browser.get(url)
satirlar = open("logininformation.txt")
satirdizisi = satirlar.readlines()
class Oturum():



    def login(self):

        anagiris=0
        username = browser.find_element_by_name("OgrNo")
        password = browser.find_element_by_name("Sifre")
        loginButton = browser.find_element_by_id('Ara')

        username.send_keys(satirdizisi[0])
        password.send_keys(satirdizisi[1])


        loginButton.click()

        self.login()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    ui = Oturum()
    ui.login()

    sys.exit(app.exec_())
