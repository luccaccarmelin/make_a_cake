print("Hello welcome to Make a Cake! here you can decide yours options to how to make a cake, and recive new finals!")
response1 = input('Do you want to play?\n')
if response1 == 'yes' or response1 == 'Yes':
    print("ok,let's start!\n")
    import time
    time.sleep(2.5)
    print("saturday")
    time.sleep(1.0)
    print("day 30")
    time.sleep(2.0)
    print("you: it's a nice day to make a cake in this morning!")
    print("you: i think this is a good idea...\n")
    time.sleep(3.8)
    print("what do you want to do?")
    print("options:\n 1:sleep \n 2:go outside \n 3:explode the house! \n 4:start to make a cake \n 5:explore the house \n 6:play a game")
    response2 = input()
    if response2 == 'sleep' or response2 == '1' or response2 == 'Sleep':
        print("you go to bed and sleep :P\n")
        print("END 01")
    elif response2 == 'go outside' or response2 == '2' or response2 == 'Go outside':
        print("you go to outside and see several things...\n")
        print("what do you want to do now?")
    elif response2 == 'explode the house!' or response2 == '3' or response2 == 'Explode the house!':
        print("you have exploded the house and die...")
        time.sleep(2.0)
        print("Moral of the story: never explode your house ¯\_(ツ)_/¯")
        print("END 05")
    elif response2 == 'start to make a cake' or response2 == '4' or response2 == 'Start to make a cake':
        print("you don't have enought ingredients...\n")
        response3 = input("Go to store or no?")
        if response3 == 'Yes' or response3 == 'yes':
            print("you go outside and see a several things...")
            time.sleep(1.0)
            print("you: wow! now i can go to the shop to buy the ingredients i need.")
        else:
            print("ok...")
    elif response2 == 'go ot outside' or response2 == '5' or response2 == 'Go outside':
        print("you go outside and see a several things...")
        time.sleep(1.0)
        print("you: wow! now i can go to the shop to buy the ingredients i need.")

        
    elif response2 == 'play a game' or response2 == '6' or response2 == 'Play a game':
        print("you play a game and became to sleep :/")
        print("END 07")
else:
     print("ok, bye bye")
