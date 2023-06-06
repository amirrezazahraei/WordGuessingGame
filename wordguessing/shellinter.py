"""this code will implement an  easy shell interface to use the 
game"""

from woge import DWGGame

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("hello welcome")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

try:
    obj = DWGGame()
except Exeption:

lang = input("enter the language:"+str(obj.languages))
obj.def_word(lang=lang)
hardness = input("enter the hardness:(HARD, INTERMEDIATE, EASY)")
obj.hardness = hardness

while (True):

    print(obj.pattern)

    word = eval(input("enter the letters of the word you guess in list:"))
    obj.giveword = word
    result = obj.check()
    cl = obj.check_left()

    if cl:
        print("rounds over sorry.")
        obj.setAsDefault()

    if result == True:
        print("you won the game")
        obj.setAsDefault()
    





