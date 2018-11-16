import PyQt5
import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore
import UI_MovieInfo

"""
File: Jeng_Winnie_Lab6.py
Author: Winnie Wei Jeng
Assignment: Lab 6
Professor: Phil Tracton
Date: 11/3/2018
Description: This simple GUI pulls up movie poster's image upon entering in the movie title

"""

# 7. no logic done here
class UI_CentralWindow(PyQt5.QtWidgets.QDialog):

    """This class holds the key GUI elements"""

    def __init__(self, parent=None):
        super(UI_CentralWindow, self).__init__(parent)  # call super on the base class

        # enterMovieLabel is a QLabel
        self.enterMovieLabel = PyQt5.QtWidgets.QLabel("Movie to Look Up")

        # entermovieLineEdit is a QLineEdit (an empty text field holder basically)
        self.enterMovieLineEdit = PyQt5.QtWidgets.QLineEdit()

        # enterMoviePush Button is a QPushButton
        self.enterMoviePushButton = PyQt5.QtWidgets.QPushButton("Look Up Movie")

        # posterLabel is a QLabel
        self.posterLabel = PyQt5.QtWidgets.QLabel("Poster Goes Here")

        # pixmap is a class member of QPixmap   https://pythonspot.com/pyqt5-image/
        self.pixmap = PyQt5.QtGui.QPixmap()

        # awardsDisplay is a class member of QTextEdit
        self.awardsDisplay = PyQt5.QtWidgets.QTextEdit()
        # awardsDisplay calls setReadOnly() method and evals to True
        self.awardsDisplay.setReadOnly(True)
        self.awardsDisplay.show()

        # vboxInfo is a VBox
        self.vboxInfo = PyQt5.QtWidgets.QVBoxLayout()

        # vbox is a VBox
        self.vbox = PyQt5.QtWidgets.QVBoxLayout()

        # hboxSearch is an HBOX
        self.hboxSearch = PyQt5.QtWidgets.QHBoxLayout()

        # # hboxInfoAndPoster is an HBOX
        self.hboxInfoAndPoster = PyQt5.QtWidgets.QHBoxLayout()

        # # hboxInfo1-5 are 5 HBOXes
        self.hboxInfo1 = PyQt5.QtWidgets.QHBoxLayout()
        self.hboxInfo2 = PyQt5.QtWidgets.QHBoxLayout()
        self.hboxInfo3 = PyQt5.QtWidgets.QHBoxLayout()
        self.hboxInfo4 = PyQt5.QtWidgets.QHBoxLayout()
        self.hboxInfo5 = PyQt5.QtWidgets.QHBoxLayout()

        # create 15 UI_MovieInfo instances in UI_CentralWindow class with corresponding titles 7-(c)-xiii-A
        self.directorInformation = UI_MovieInfo.UI_MovieInfo(title="Director:")  # 7-(c)-xiii-A
        self.actorInformation = UI_MovieInfo.UI_MovieInfo(title="Actor:")
        self.releaseDateInformation = UI_MovieInfo.UI_MovieInfo(title="Release Date:")

        self.budgetInformation = UI_MovieInfo.UI_MovieInfo(title="Budget:")  # 7-(c)-xiii-A
        self.revenueInformation = UI_MovieInfo.UI_MovieInfo(title="Revenue:")
        self.runTimeInformation = UI_MovieInfo.UI_MovieInfo(title="Run Time:")

        self.voteCountInformation = UI_MovieInfo.UI_MovieInfo(title="Vote Count:")
        self.voteAverageInformation = UI_MovieInfo.UI_MovieInfo(title="Vote Average:")
        self.statusInformation = UI_MovieInfo.UI_MovieInfo(title="Status:")

        self.monthlyRevenueMeanInformation = UI_MovieInfo.UI_MovieInfo(title="Monthly Revenue Mean:")
        self.monthlyRevenueMedianInformation = UI_MovieInfo.UI_MovieInfo(title="Monthly Revenue Median:")
        self.monthlyRevenueStdInformation = UI_MovieInfo.UI_MovieInfo(title="Monthly Revenue STD:")

        self.annualRevenueMeanInformation = UI_MovieInfo.UI_MovieInfo(title="Annual Revenue Mean:")
        self.annualRevenueMedianInformation = UI_MovieInfo.UI_MovieInfo(title="Annual Revenue Median:")
        self.annualRevenueStdInformation = UI_MovieInfo.UI_MovieInfo(title="Annual Revenue STD:")

        # add to hboxSearch, using addWidget() method, the 3 QMethods declared at the top of the class:
        #  MovieLabel, MovieLineEdit, MoviePushButton
        self.hboxSearch.addWidget(self.enterMovieLabel)
        self.hboxSearch.addWidget(self.enterMovieLineEdit)
        self.hboxSearch.addWidget(self.enterMoviePushButton)

        # ? 7.(C)-xv
        # add to hboxInfo1, using getLayout() method, three of the 15 UI_Movie instances
        self.hboxInfo1.addLayout(self.directorInformation.getLayout())
        self.hboxInfo1.addLayout(self.actorInformation.getLayout())
        self.hboxInfo1.addLayout(self.releaseDateInformation.getLayout())

        # likewise, add to hboxInfo2
        self.hboxInfo2.addLayout(self.budgetInformation.getLayout())
        self.hboxInfo2.addLayout(self.revenueInformation.getLayout())
        self.hboxInfo2.addLayout(self.runTimeInformation.getLayout())

        # likewise, add to hboxInfo3
        self.hboxInfo3.addLayout(self.voteCountInformation.getLayout())
        self.hboxInfo3.addLayout(self.voteAverageInformation.getLayout())
        self.hboxInfo3.addLayout(self.statusInformation.getLayout())

        # likewise, add to hboxInfo4
        self.hboxInfo4.addLayout(self.monthlyRevenueMeanInformation.getLayout())
        self.hboxInfo4.addLayout(self.monthlyRevenueMedianInformation.getLayout())
        self.hboxInfo4.addLayout(self.monthlyRevenueStdInformation.getLayout())

        # likewise, add to hboxInfo5
        self.hboxInfo5.addLayout(self.annualRevenueMeanInformation.getLayout())
        self.hboxInfo5.addLayout(self.annualRevenueMedianInformation.getLayout())
        self.hboxInfo5.addLayout(self.annualRevenueStdInformation.getLayout())

        # for hboxInfoAndPoster, addWidget for posterLabel and awardsDisplay
        self.hboxInfoAndPoster.addWidget(self.posterLabel)
        self.hboxInfoAndPoster.addWidget(self.awardsDisplay)

        # for vboxInfo, use addLayout() method to add in hboxInfo 1-5
        self.vboxInfo.addLayout(self.hboxInfo1)
        self.vboxInfo.addLayout(self.hboxInfo2)
        self.vboxInfo.addLayout(self.hboxInfo3)
        self.vboxInfo.addLayout(self.hboxInfo4)
        self.vboxInfo.addLayout(self.hboxInfo5)

        # 7-(c)-xxii
        # for hboxInfoAndPoster, add in vboxInfo using addLayout() method
        self.hboxInfoAndPoster.addLayout(self.vboxInfo)

        # for vbox, add in hboxSearch and hboxInfoAndPoster using addLayout() method
        self.vbox.addLayout(self.hboxSearch)
        self.vbox.addLayout(self.hboxInfoAndPoster)

        # setLayout to vbox
        self.setLayout(self.vbox)

    # 7-(d) update poster upon click button Look up moive?
    def updatePoster(self, posterFileName=None):

        """This moethod loads the specified poster name into the GUI"""

        # load the posterFileName instance into pixmap
        self.pixmap.load(posterFileName)  # ? 7-(d)-i something /Poster/img_name.jpg

        # scaled the pixmap image via scaled() method using posterLabel size and KeepAspectRatio
        self.pixmap.scaled(self.posterLabel.width(), self.posterLabel.height(), PyQt5.QtCore.Qt.KeepAspectRatio)

        # call setPixmap of the posterLabel with pixmap
        self.posterLabel.setPixmap(self.pixmap)  # what does it mean?

        # for posterLabel, set scaled content to false
        self.posterLabel.setScaledContents(False)