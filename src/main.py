import sys
import os
from PyQt6 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt6.QtWebEngineCore import QWebEngineSettings

PDF = os.getcwd() + '/resources/link-analysis.pdf'

class Window(QtWebEngineWidgets.QWebEngineView):
    def __init__(self):
        super().__init__()
        self.settings().setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.WebAttribute.PdfViewerEnabled, True)
        print(QtCore.QUrl.fromUserInput(PDF))
        self.load(QtCore.QUrl.fromUserInput(PDF))

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.showMaximized()
    sys.exit(app.exec())