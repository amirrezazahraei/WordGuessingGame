"""this code will implement an  easy shell interface to use the 
game"""
import sys
from woge import DWGGame

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("hello welcome")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

try:
    obj = DWGGame()

except Exception:
    print("An error occurred while openning the data")
    sys.exit()

def get_data():
    """this method will get the data from the user to start the game"""



    while True:

        lang = input("enter the language:"+str(obj.languages))
        hardness = input("enter the hardness:(HARD, INTERMEDIATE, EASY)")

        if lang in obj.languages and hardness in obj.GameModes:
            break
        else:
            print("sorry an error occured")

    obj.def_word(lang=lang)#the sequence here is really important because we need to first
    # define the word and then based on it's length define the hardness
    obj.hardness = hardness
    

get_data()

while True:

    print(obj.pattern)
    print(obj.left,"rounds left.")
    
    word = eval(input("enter the letters of the word you guess in list:"))
    is_continue = input("enter any thing rather than 0 to continue:")
    if is_continue == '0':
        break
    obj.giveword = word
    result = obj.check()
    cl = obj.check_left()


    if cl:
        print("rounds over sorry.")
        obj.setAsDefault()

    if result is True:
        print("you won the game")
        obj.setAsDefault()
        get_data()




