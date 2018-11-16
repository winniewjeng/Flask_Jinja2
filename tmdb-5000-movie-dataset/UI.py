import PyQt5.QtWidgets
import UI_CentralWindow
import OpenMovie
import json
import logging
import sys
import sqlalchemy

"""
File: Jeng_Winnie_Lab6.py
Author: Winnie Wei Jeng
Assignment: Lab 6
Professor: Phil Tracton
Date: 11/3/2018
Description: This simple GUI pulls up movie poster's image upon entering in the movie title

"""

# 8.
class UI(PyQt5.QtWidgets.QMainWindow):
    """
    This class contains the top level UI module that
     connects together the various top level items and signals.
    """

    def __init__(self, moviesJSON=None, parent=None):
        # self.count = 0  # keep for purpose of testing button
        # moviesJSON in the JSON instance from lab6.py
        super(UI, self).__init__(parent)

        # store the input moviesJSON in a class member of the same name
        self.moviesJSON = moviesJSON

        # set the window title
        self.setWindowTitle("Python Movie Project")

        # set the status bar's message
        self.statusBar().showMessage("Status Bar")  # ? 8-(d)-4

        # 8-(d)-v
        # class member centralWidget is an instance of UI_CentralWindow
        self.centralWidget = UI_CentralWindow.UI_CentralWindow()

        """connect the PushButton from our central widget to a handler"""
        # 8-(d)-vi
        self.centralWidget.enterMoviePushButton.clicked.connect(self.enterMoviePushButtonClicked)  # 7-(d)-vi

        # show the UI?
        self.centralWidget.show()

    # when the enterMovie button is triggered...
    def enterMoviePushButtonClicked(self):
        # read the movieTitle from enterMovieLineEdit with text() method
        self.movieTitle = self.centralWidget.enterMovieLineEdit.text()

        # create an instance of posterURL from the movies.json data structure
        contents = open('movies.json', 'r')
        data = json.load(contents)
        for i in data['movie_posters']:
            if i == self.movieTitle:
                # i is self.movieTite and data['movie_posters'][i] is URL
                openMovie = OpenMovie.OpenMovie(self.movieTitle, data['movie_posters'][i])
            else:
                # create an instance of openMovie from the movies.json data structure
                logging.error(" cannot find the poster URL")
                openMovie = OpenMovie.OpenMovie(self.movieTitle, posterURL=None)

        # store in movieTitleQuery the results of the getMovieTitleData method call from our openMovie instance.
        movieTitleQuery = openMovie.getMovieTitleData()
        if movieTitleQuery is False:
            return



        # """UNCLEAR"""
        # posterURL =
        # #  The keys of ”movie posters” and the movieTitle
        # # you just read will give you the URL
        #
        # # store in movieTitleQuery the results of the getMovieTitleData method call from our openMovie instance.
        # movieTitleQuery = openMovie.getMovieTitleData()
        #
        # if movieTitleQuery is False:
        #     return
        #
        # cast = openMovie.getCast()
        # crew = openMovie.getCrew()  # get director and crew


        """" comment out the code that gets posterURL from json, as we're now gettign the code from the db"""
        print(self.movieTitle)

        """The rest below is all very ambiguous"""

        try:
            contents = open('movies.json', 'r')

        except:
            print("Failed to open JSON file")
            logging.error(" Failed to open JSON file")
            sys.exit()

        # data is a dictionary loaded from the ”movie_posters” field of json data
        data = json.load(contents)

        # check if movieTitle is in json data "movie_posters" list of keys
        for i in data['movie_posters']:
            # self.count = self.count + 1  # keep for purpose of testing button
            if self.movieTitle == i:
                # i is self.movieTite and data['movie_posters'][i] is URL
                instance = OpenMovie.OpenMovie(i, data['movie_posters'][i])
                if instance.getPoster() is False:
                    return
                else:
                    self.centralWidget.updatePoster(instance.posterFileName)
            else:
                pass

        contents.close()





