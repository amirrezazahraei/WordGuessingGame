"""this code file will use the words to select one of them 
for the game. it will select the first word of the csv file
and then push it at the end of the file."""

from data_path_reader import open_file
import csv

class ChooseWord:
    """this class choose word!"""

    def __init__(self):
        self.languages, self.paths = open_file()