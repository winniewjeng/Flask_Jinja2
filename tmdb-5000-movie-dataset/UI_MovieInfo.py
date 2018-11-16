import PyQt5
import PyQt5.QtWidgets
import PyQt5.QtGui

"""
File: Jeng_Winnie_Lab6.py
Author: Winnie Wei Jeng
Assignment: Lab 6
Professor: Phil Tracton
Date: 11/3/2018
Description: This simple GUI pulls up movie poster's image upon entering in the movie title

"""

# 6
class UI_MovieInfo(PyQt5.QtWidgets.QDialog):
    """
    this level holds together a few GUI elements that get repeated several times
    """

    def __init__(self, parent=None, title=None):

        super(UI_MovieInfo, self).__init__(parent)

        self.title = title
        self.hBox = PyQt5.QtWidgets.QHBoxLayout()  # 6-(c)-iii

        # make a title label
        self.titleLabel = PyQt5.QtWidgets.QLabel(self.title, self)  # iv
        # customize the label font
        self.titleLabelFont = PyQt5.QtGui.QFont()  # v
        self.titleLabelFont.setBold(True)  # v
        self.titleLabel.setFont(self.titleLabelFont)  # ? 6.(C)-vi--set BOLD font

        # make an info label
        self.infoLabel = PyQt5.QtWidgets.QLabel("info", self)  # vii

        self.hBox.addWidget(self.titleLabel)
        self.hBox.addWidget(self.infoLabel)

    def getLayout(self):  # (d)
        return self.hBox
