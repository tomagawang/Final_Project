from audioop import mul
from pprint import pprint
from multiple_choice import multiple_choice
from apis import get_love
import sentiment

def act2_01():
    '''part 1 of act 1'''
    pprint('After helping your son with his homework, you board your helicopter and heads for work accompanied by your butler. On the helicopter, your butler talks about his intend for resignation. The butler shares some grewsome news about her daughter committing suicide. He has always been distant from his family. He had no clue that her daughter suffered from depression until now. He wants to spend more time from his family from now on. He understood about this good paying job, but he wants to be with his family in this season and takes some time to grief, he will leave at the end of the month. You express your condolences to the Butler and accept his resignition.')
    pprint('As you arrive at your desk, you sit and pondering your future. As you are reading through your emails, you spot your old draft for resignation. You open it and decide finally to finish it.')
    pprint("After a board meeting, you decide to talk to the chairmen in private.")
    pprint("Make a choice; A: Hand him the resignition letter and leave. B: Hand him the resignition letter and wait for his response. ")
    answer = multiple_choice()
    if answer == 0:
        pprint("You left the company without saying anything, the chairmen is very confused.")
        return 0
    if answer == 1:
        pprint("The chairmen is surprised about this news. He cannot understand why you want to quit. The chairmen rejects the resignation letter and asks you to reconsider your decision and talk to him again tomorrow.")
        return 1

def act2_02():
    '''part 2 of act 2'''
    pprint("You return home and is ready to tell your family your decision to quit. However, the house is darkened and quiet. The maid is washing and clearing the dishes. Your wife is smoking and drinking wine on the balcony. Your daughter is back from college and sits in the dining room looking dejected. You greet your daughter, but she stays quiet and distant. You reaches out to your wife and see what's going on, she reveal to you that your daughter is pregnant, she thinks she should just get an abortion, but your daughter refuses.")
    pprint("Make a choice; A: support your wife, and talk to your daughter about the abortion. B: support your daughter and try to convince your wife. ")
    answer = multiple_choice()
    if answer == 0:
        pprint("Your wife is actually dissapointed because she thought you actually had a heart. She really had enough of this marriage and she wants a divorse.")
        return 0
    if answer == 1:
        input1 = input("try to say something to convince your wife:")
        posi = sentiment.natural_language_processing(input1)
        if posi == 0:
            pprint("You were not very convincing, but your wife understands your point and appreciate that you care about your daughter.")
            return 1
        if posi == 1:
            pprint("You actually made your wife very happy, she kisses you and appreciate your care for your daughter.")
            return 2

def act2_03():
    '''part 3 of act 2'''
    pprint("Your wife hands you the divorse papers she prepared earlier and continues to drink her wine.")
    pprint("Make a choice; A: Accept the divorse papers. B: Reveal to your wife about your decision to quit your job")
    answer = multiple_choice()
    if answer == 0:
        pprint("Your wife walks away, she can't believe you actually accepted the divorse papers.")
        return 0
    if answer == 1:
        pprint("Your wife is quite moody at the moment, but she is surprised that you decides to quit the job, but she still wants to get a divorse.")
        pprint("Enter your wife's name for a compatibility test")
        input1 = input("First, remind me your name:")
        input2 = input("Now, enter a name for your wife:")
        percent = get_love(input1, input2)


def main():
    pass

if __name__ == "__main__":
    main()