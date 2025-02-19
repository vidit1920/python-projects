import random
name=input("Enter your name :")
print(" ***** RULES ******* \n"
      "you will get 6 chances and if you type an incorrect letter \n"
      "your chances will be deducted and once it reaches 0 you will lose \n"
      "we will display your incorrect guess if you type an incorrect letter")
print("**************************************************")
print("Let's play hangman game",name,"Best of luck!!")
fruit=( "apple", "banana", "orange", "grapes", "pineapple", "mango", "strawberry", "blueberry", 
    "watermelon", "papaya", "peach", "cherry", "kiwi", "plum", "pomegranate", "avocado", 
    "lemon", "lime", "coconut", "dragonfruit", "raspberry", "blackberry", "lychee", "apricot", 
    "guava", "pear", "melon", "cantaloupe", "fig", "tangerine", "nectarine", "date", "mandarin", 
    "jackfruit", "cranberry", "currant", "starfruit", "longan", "passionfruit", "quince", 
    "soursop", "mulberry", "zucchini", "gooseberry", "salak", "hornedmelon", "breadfruit", 
    "acai", "custardapple", "bittermelon", "chico", "pomelo", "carambola")

vegetable=("carrot", "broccoli", "spinach", "lettuce", "cucumber", "tomato", "bellpepper", 
    "cauliflower", "zucchini", "cabbage", "peas", "greenbeans", "potato", "sweet potato", 
    "onion", "garlic", "radish", "eggplant", "asparagus", "artichoke", "kale", "brusselssprouts", 
    "celery", "pumpkin", "butternutsquash", "beetroot", "leek", "chard", "bok choy", 
    "fennel", "endive", "collardgreens", "parsnip", "rutabaga", "turnip", "snowpeas", 
    "swisschard", "okra", "mushroom", "alfalfasprouts", "arugula", "watercress", "scallions", 
    "shallots", "chillpepper", "horseradish", "taro", "edamame", "chayote", "daikon", 
    "napacabbage", "tatsoi")
color=("red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", 
    "white", "gray", "violet", "indigo", "cyan", "magenta", "beige", "turquoise", "lavender", 
    "gold", "silver", "bronze", "peach", "teal", "mint", "lime", "coral", "charcoal", 
    "navy", "emerald", "fuchsia", "amber", "scarlet", "ivory", "tan", "plum", "rose", 
    "crimson", "khaki", "chartreuse", "azure", "ruby", "sage", "olive", "mauve", "ivory", 
    "salmon", "periwinkle", "mustard", "electricblue", "royalblue", "sunflower", "aqua")
l=(fruit,vegetable,color)
ran1=random.choice(l)
ran=random.choice(ran1)

stage={ 
           1:("|------ ",
              "|     | ",
              "|       ",
              "|       ",
              "|       ",
              "|       ",
              "|       "),
           2:("|------ ",
              "|     | ",
              "|     O ",
              "|       ",
              "|       ",
              "|       ",
              "|       "),
           3:("|------  ",
              "|     |  ",
              "|     O  ",
              "|      / ",
              "|        ",
              "|        ",
              "|        "),
           4:("|------  ",
              "|     |  ",
              "|     O  ",
              "|    \\ / ",
              "|        ",
              "|        ",
              "|        "),
           5:("|------  ",
              "|     |  ",
              "|     O  ",
              "|    \\ / ",
              "|     |  ",
              "|        ",
              "|        "),
           6:("|------  ",
              "|     |  ",
              "|     O  ",
              "|    \\ / ",
              "|     |  ",
              "|    /   ",
              "|        "),
           7:("|------  ",
              "|     |  ",
              "|     O  ",
              "|    \\ / ",
              "|     |  ",
              "|    / \\ ",
              "|        ")
        }
count=0
def hint(hints):
    print(' '.join(hints))
    
hints=['_']*len(ran)
if ran1==fruit:
    print("The word is a type of fruit")
elif ran1==color:
    print("The word is a type of color")
elif ran1==vegetable:
    print("The word is a type of vegetable")
while count<8:
    print("****************************")
    hint(hints)
    print("****************************")
    guess=input("guess the word :").lower()
    if guess in ran:
        for i in range(len(ran)):
            if ran[i]==guess:
                hints[i]=guess
    elif guess not in ran:
        count+=1
        print("no of incorrect guesses",count)
        if count==1:
            print('\n'.join(stage[1]))
        if count==2:
            print('\n'.join(stage[2]))
        if count==3:
            print('\n'.join(stage[3]))
        if count==4:
            print('\n'.join(stage[4]))
        if count==5:
            print('\n'.join(stage[5]))
        if count==6:
            print('\n'.join(stage[6]))                  
        if count==7:
            print('\n'.join(stage[7]))
            print("Sorry",name,"You lost try again")
            print("The word was",ran)
            break
    if guess==ran:
        print("Congrats, you WON!!!",name)
        break



