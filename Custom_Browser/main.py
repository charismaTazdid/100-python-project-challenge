import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
# navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        previous_btn = QAction("Previous", self)
        previous_btn.triggered.connect(self.browser.back)
        navbar.addAction(previous_btn)

        next_btn = QAction("Next", self)
        next_btn.triggered.connect(self.browser.forward)
        navbar.addAction(next_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.search_bar = QLineEdit()
        self.search_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.search_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://google.com"))

    def navigate_to_url(self):
        url = self.search_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, url):
        self.search_bar.setText(url.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName("Your Won Browser")
window = MainWindow()
app.exec_()
