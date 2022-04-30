from pprint import pprint
from multiple_choice import multiple_choice
import sentiment
from apis import get_insult
from math_game import math_game

def opening():
    pprint("""You are the CFO of Colson Group; you are currently striking a deal to purchase an manufacturing plant. The seller offer is $1500000, but you believe the value of manufacturing plant is only about $1000000, and your company do not wish to pay more than $250000 in premium. You were given $1250000, you can't pay more than that. Your latest offer was $900000. Seller says: $1450000 is our last offer. If you do not take it, then we will look for someone else.""")


def act1_01():
    '''part 1 of act 1'''
    pprint('''After you finished your work, you walk on the helipad and boards your luxurious helicopter home. Your butler awaits you and assists you boarding the helicopter. You enjoy a helicopter ride cruising down the city lights and busy streets and suddenly arrives at a mansion on the cliff of a mountain hill. After you landed, you saw your family gathering around a table and singing Happy Birthday to your son. You forgot it is his birthday today which your wife reminded you this morning.''')
    pprint('''Choose A: Lie to your son and tell him that his birthday gift is late. B: Be honest with your son and apologize.''')
    answer1 = multiple_choice()
    if answer1 == 0:
        pprint('''Your son says he does not want anything from you because he knows you are lying and you never really cared about him. After a brief birthday session, he returns to his room promptly''')
        pprint('The following morning. While you are enjoying your breakfast. You saw the maid giving your son some medicine. You ask the maid what that medicine is, the maid looks at your son. Your son says that you would know if you paid just a little more attention to your family. Son says to Mr. Park that there is one wish, he just hopes that Mr. Park would care about his family more, and son left the table.')
        return 0
    if answer1 == 1:
        pprint("Your son says he forgives you. You and your son had a great night together.")
        pprint('The next morning, while you are enjoying your breakfast. You saw the maid giving your son some medicine. You ask the maid what that medicine is, the maid looks at your son. Your son says that there is only one wish for his birthday, he just hopes that your would care more about your family, and then he left the table.')
        return 1

def act1_02():
    '''part 2 of act 1'''
    pprint("You decides to check on your son. His bedroom door is locked, but you can hear that he is playing video games. You knocks on it a few times, there is no answer.")
    input1 = input("Say something to your son to convince him to open the door:")
    posi = sentiment.natural_language_processing(input1)
    if posi == 1:
        pprint("Your son opens the door and ask you what you want, you tell him that you just want to talk to him.")
        act1_03()
    else:
        pprint('Still have no answer. After a little bit...')
        act1_02()

def act1_03():
    '''part 3 of act 1'''
    pprint("You ask your son what's going on and why is he on antidepressant medication. He shows you a piece of paper that writes:")
    print(get_insult())
    pprint("You ask your son, why would he write that? He tells you that his classmates left this in his locker, and this isn't the first time.")
    pprint("You pause for a minute, and thinks about what you are going to say to him.")
    input1 = input("Say something to encourage your son:")
    posi = sentiment.natural_language_processing(input1)
    if posi == 1:
        pprint("Your son says thank youtells you that he really hope you could talk with him more like this in the future. He tells you that he is also behind on his math homework and asks you to help him.")
        pprint('''Choose A: Encourage your son that he can figure out the answers himself. B: Help him with his homework.''')
        answer1 = multiple_choice()
        if answer1 == 0:
            return 2
        else:
            result = math_game()
            if result == 2:
                return 3
            if result == 1:
                return 2
            else:
                return 0
    else:
        pprint('Your son remains quiet and continues to play vidoe games. You are not sure what to do, so you left for work.')
        return 0


def main():
    act1_03()
if __name__ == "__main__":
    main()
