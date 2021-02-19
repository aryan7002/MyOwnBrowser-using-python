#pyqt5 module 56.9 mb
#PyQtWebEngine module(pip install PyQtWebEngine) 60.2 mb

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngine import *
from PyQt5.QtWebEngineWidgets import *
import sys   #inbuilt

class MainWindow(QMainWindow): # mai window class
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView() #it will open view of browser
        self.browser.setUrl(QUrl('https://www.google.com/'))#this link will open in browser
        self.setCentralWidget(self.browser)
        self.showMaximized() #for full screen mode

        #navbar
        navbar=QToolBar()#defining toll bar provided by package
        self.addToolBar(navbar)#adding navbar to browser

        #adding back button to browser
        back =QAction('Back',self)#declaring back button and saying you have to take some action
        back.triggered.connect(self.browser.back)#adding method to go back page provided by package
        navbar.addAction(back)#adding back button that we have created to navbar

        #adding forward button to browser
        forward =QAction('Forward',self)#declaring forwad button and saying you have to take some action
        forward.triggered.connect(self.browser.forward)#adding method to go forward a page
        navbar.addAction(forward)#adding forward buton to nav bar

        #addding refresh button
        reload = QAction('Reload',self)#declaring reload button and saying you have to take some action
        reload.triggered.connect(self.browser.reload)#adding method to reload  a page
        navbar.addAction(reload)#adding reload buton to nav bar

        #adding home button
        home = QAction('Home',self)#declaring home button and saying you have to take some action
        home.triggered.connect(self.navigate_home)#adding method to go back home(connect meanse click method)
        navbar.addAction(home)#adding home buton to nav bar

        #adding url bar
        self.url_bar=QLineEdit()#this is genrally textbox
        self.url_bar.returnPressed.connect(self.navigate_url)#creatting userdefine function to add funcnality to textbox
        navbar.addWidget(self.url_bar)#caaling user define function

        #adding serch box

        serchbox = QAction('Serch', self)
        serchbox.triggered.connect(self.navigate_url)
        navbar.addAction(serchbox)


        self.browser.urlChanged.connect(self.update_url)#userdefine function to upadte url

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com/'))#you can set any website as home page

    def navigate_url(self):
        url = self.url_bar.text()#geeting text from QLineEdit
        self.browser.setUrl(QUrl('http://'+url))#only serch sitename with .com extension or any other

    def update_url(self,q):
        self.url_bar.setText(q.toString())#to confirm the url is in string format




app=QApplication(sys.argv)#argv parameter is required so sys.argv
QApplication.setApplicationName("Aryan Browser") # name of your browser
window= MainWindow()#class main window
app.exec_()#it will execute window