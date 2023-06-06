"""this file impelements the easy logic of the program"""
from data import ChooseWord
import random

class DWGGame(ChooseWord):
    """this is a class that  impelements the data of the wordguessing game
    how to use the following class:
    1 - first run the def_word
    2 - define the hardness of the game
    3 - now that you are done givving data and you should start 
    the game
    4 - first give a word
    5 - then when you are sure of your givven word run the check
    6 after that run the check_left
    7 - if the rounds are over the check_left will say
    8 - if you won the check will give you
    9 - for playing the next game run the setASDefault method"""

    __word:list = []
    pattern:list = []
    len_word:int = 0
    __giveword:list = []
    __hardness:int = 0
    GameModes = ['EASY', 'HARD', 'INTERMEDIATE']
    __left:int = 0 # this is used for counting down

    def __init__(self):
        super().__init__()

    def def_word(self, lang):
        """this method will choose a word based on the givven language
        and then it will parse it  into a list of words"""
        word = self.pick(language=lang)
        for letter in word[0]:
            if letter == " ":
                self.pattern.append(' ')
            else:
                self.pattern.append("x")
            self.__word.append(letter)
        self.len_word = len(self.__word)

    @property
    def hardness(self):
        return self.__hardness
    
    @hardness.setter
    def hardness(self, other):

        if other == "HARD":
            self.__hardness=random.randint(self.len_word+5, self.len_word+10)

        elif other == "INTERMEDIATE":
            self.__hardness=random.randint(self.len_word*2, self.len_word*3)
        
        elif other =="EASY":
            self.__hardness=random.randint(self.len_word**2, self.len_word**2+20)

        else:
            raise ValueError("the givven input must be(HARD, INTERMEDIATE, EASY)")
        self.__left = self.__hardness

    @property
    def left(self):
        return self.__left

    @property
    def giveword(self):
        return self.__giveword
    
    @giveword.setter
    def giveword(self, other:list):
        print(len(other), self.len_word, other)
        if len(other) == self.len_word:
            self.__giveword = other
        else:
            raise TypeError("the givven input must have the same length as thr picked word")
        
    def setAsDefault(self):
        """this method will set all the variables"""
        self.__word = []
        self.__giveword = []
        self.__hardness = 0
        self.__left = 0
        self.pattern = []
        self.len_word = 0

    def check_left(self):

        if self.__left < 1:
            return True
        else:
            return False

    def check(self):
        """this method will check weather the givven word
        and the word are equal or no"""

        index = -1
        indexs = []

        for k in range(self.len_word):
            i, j = self.__word[k], self.__giveword[k]
            index+=1
            if i == j:
                self.pattern[index] = i
                indexs.append(index)

        self.__left -= 1

        if len(indexs) == self.len_word:
            return True
        else:
            return  indexs
        
        
            





    

    

    

    

        
    

    

