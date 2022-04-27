import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser= QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        navbar =QToolBar()
        self.addToolBar(navbar)

        backbutton =QAction('BACK',self)
        backbutton.triggered.connect(self.browser.back)
        navbar.addAction(backbutton)
        forward =QAction('forward',self)
        forward.triggered.connect(self.browser.forward)
        navbar.addAction(forward)
        reload= QAction('reload',self)
        reload.triggered.connect(self.browser.reload)
        navbar.addAction(reload)
        homebutton= QAction('Home',self)
        homebutton.triggered.connect(self.navigate_home)
        navbar.addAction(homebutton)
        self.url_bar =QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)
    def update_url(self,q):
        self.url_bar.setText(q.toString())
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))
    def navigate_to_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))

app= QApplication(sys.argv)
QApplication.setApplicationName("Biswojit Browser")
window = MainWindow()
app.exec_()
