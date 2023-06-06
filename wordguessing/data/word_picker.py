"""this code file will use the words to select one of them 
for the game. it will select the first word of the csv file
and then push it at the end of the file."""

import csv
import data.data_path_reader


class ChooseWord:
    """this class choose word!"""

    languages:list
    paths:list

    def __init__(self):
        self.languages, self.paths = data.data_path_reader.open_file()# thiss p

    def open_csv(self, path_index):
        """this method will open the csv. the path_index
        is the index of the path in self.paths list"""

        with open(self.paths[path_index], mode = 'r', encoding="utf-8") as file:
            read = csv.reader(file)
            read = list(read)
        
        return read
    

    def write_csv(self, data_, path_index):
        """this method will get """
        with open(self.paths[path_index], mode='w', encoding='utf-8') as file:
            write=csv.writer(file)
            write.writerows(data_)

    def pick(self, language:str):
        """this method will pick a word from the data.
        if the output of method was False it means language is
        not supported"""

        if language not in self.languages:
            raise ValueError("the givven language is not supported") # means that the language is not  supported
        
        index = self.languages.index(language)
        data_ = self.open_csv(index)

        word = data_[1] # this will get the first word of the 
        # data. it uses 1 because the first index is occupied 
        # b the field

        data_.append(data_[1])
        data_.pop(1)

        self.write_csv(data_, index)

        return word





    

    


