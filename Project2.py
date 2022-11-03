#Adrianne Verstraete
import time
import random
out=[]
element=""


def prt_list(list):
    for x in list:
        print(x, flush=True)
        if len(x)<70:
            time.sleep(2)
        else:
            time.sleep(3)


def prt_single(sentence,num):
    print(sentence, flush=True)
    time.sleep(num)


#The initial story.
def intro():
    global element
    element= random.choice(["cleans","deadlifts","squats", "snatches"])
    story=[
    "You find yourself entering a crossfit gym.","Coach talks about the lifts"
    "we are performing today.", f"He tells us we can pick between {element}"
    "or {element}.",
    "In the front one group picks the first lift.",
    "Behind you os another group  who picked the second lift",
    "In your hands you have a barbell.\n"
        ]
    prt_list(story)


#The player chooses whether they go to the group in front of them or behind
#them.
def choose_1():
    act=[
        "Enter 1 to join the group in front of you.",
        "Enter 2 to join the group behind you.", "What would you do?""
        ]
    prt_list(act)
    response=str(input("(please enter 1 or 2.)\n"))
    return response


#Related to the case player chose number 2, joining the group behind them,
#in choose_1.
def choose_11():
    act11=[
        "You approach the group behind you.",
        f"You pick up your barbell and begin practicing the {element} with"
        f"your group. You put on two plates to start heavy"
        ]
    act1=[
        "You pick up the barbell. The coach explains how  to do the lift"
        f"Someone exclaims that the {element} are so difficult to do!",
        f"You get nervous and feel like you will mess up",
        "So you  only use  an empty barbell to begin with."]
    if "barbell" in out:
        prt_list(act11)
    else:
        prt_list(act1)
    response1=str(input("Would you like to (1) start heavy or (2) start"
    "light?\n"))
    return response1


#Related to the answer for the choose_11, either start heavy or start light.
def choose_111():
    response1=choose_11()
    if response1=="1":
        act3=[
            "You do your best...", f"But your body is in pain and not able to"
            f"handle the heavy weight for the {element}.", "You have failed it.\n"
            ]
        act 4=[
        "You start at a light weight and you are able to do more reps with"
        f"the barbell.", "Your body feels great and you can do the {element}"
        f"more efficiently!\n"
        ]
    if "barbell" in out:
        prt_list(act4)
        play_again()
    else:
        prt_list(act3)
        play_again()
    elif response1=="2":
        prt_single(
        "You start building to heavy weights unsure if you can do it,2"
        )
    else:
        prt_single("No! Stay at a lighter weight!,2")
        choose_111()


#Related to the case whenplayer chose number 2, starting lighter,
#in chose_1.
def choose_12():
    prt_single("You slowly build, not going super heavy.,2")
    act2=[
        "You are success in completing the amount of reps at a reasonable",
        f"weight without hurting your body and compromising form!\n"
        ]
    if "barbell" in out:
        prt_single("You have done this for a single rep, now do many.,2")
        prt_single("You go back down in weight.,2")
    else:
        prt_list(act2)
        out.append("barbell")


def game():
    response=choose_1()
    if response=="1":
        choose_111()
    elif response=="2":
        choose_12()
    else:
        game()
    game()


#Adventure game.
def Adventure():
    intro()
    game()
    play_again()


#Playing again.
def play_again():
    global aboutprt_single("Would you like to play again?,2")
    response2=str(input("Please enter y for yes and n for no.\n").lower())
    if response2=="y":
        out=[]
        Adventure()
    elif response2=="n":
        exit()
    else:
        play_again()


Adventure()
