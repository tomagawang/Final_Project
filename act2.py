from audioop import mul
from pprint import pprint
from multiple_choice import multiple_choice
from apis import get_love
import sentiment

def act2_01():
    '''part 1 of act 1'''
    pprint('After interacting with your son, you board your helicopter and head for work accompanied by your butler. On the helicopter, your butler asks you for permission to resign. The butler shares the grewsome news that his daughter committed suicide. He has always been distant from his family. He had no clue that her daughter suffered from depression until now. He wants to spend more time from his family from now on. He understands that he has a good paying job, but he wants to be with his family in this season and takes some time to grief, he will leave at the end of the month. You express your condolences to the Butler and accept his resignition.')
    pprint('As you arrive at your desk, you ponder about your future. As you are reading through your emails, you spot an old draft of resignation letter. You open it and decide to finally finish it.')
    pprint("After a board meeting, you ask the chairmen to speak in private.")
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
    pprint("You return home and are excited to tell your family about your decision to quit. However, the house is darkened and quiet. The maid is washing and clearing the dishes. Your wife is smoking and drinking wine on the balcony. Your daughter is back from college and sits in the dining room looking dejected. You greet your daughter, but she stays quiet and distant. You reaches out to your wife and see what's going on, she reveals to you that your daughter is pregnant, she thinks she should just get an abortion, but your daughter refused.")
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
            pprint("Your wife were convinced, and you actually made her very happy;she kisses you and appreciate your care for your daughter.")
            return 2

def act2_03():
    '''part 3 of act 2'''
    pprint("Your wife hands you the divorse papers that she prepared earlier and continues to drink her wine.")
    pprint("Make a choice; A: Accept the divorse papers. B: Reveal to your wife about your decision to quit your job")
    answer = multiple_choice()
    if answer == 0:
        pprint("Your wife walks away, she can't believe you actually accepted the divorse papers.")
        return 0
    if answer == 1:
        pprint("Your wife is quite moody at the moment, but she is surprised that you decides to quit the job. However, she still wants to get a divorse.")
        pprint("There may still be hope for your marriage, enter your names for a compatibility test")
        input1 = input("First, remind me your name:")
        input2 = input("Now, enter a name for your wife:")
        percent = int(get_love(input1, input2))
        if percent > 60:
            pprint("You are quite compatible with your wife, there is still hope for your marriage.")
            return 2
        else:
            pprint("You are not really compatible with your wife, but there may still be hope to save your marriage.")
            return 1

def act2_04():
    '''part 3 of act 2'''
    pprint("""Second day at work, you express to the chairmen again that you have made up your mind that you need to quit. The chairmen pulls out his contract and shows you that quitting before the contract expiration will have penalty. You needs to pay 5 million dollars for company losses. The chairmen has spoken with the board and they are willing to give Mr. Park a 3 million dollar raise next year.""")
    pprint("Make a choice: A: accept the company offer. B: reject the company offer and pay the 5 million dollars")
    answer = multiple_choice()
    if answer == 1:
        pprint("""The chairmen says that he can raise your raise next year to 5 million dollars.""")
        pprint("Make a choice: A: accept the chairmen's offer. B: reject the chairmen's offer.")
        answer = multiple_choice()
        if answer == 0:
            pprint("The chairmen is very happy with your decision and promised to have a super model to be your personl assistant moving forward")
            return 2
        if answer == 1:
            pprint("The chairmen then pulls out a series of pictures of you having affairs with your ex-assistant. He threatens you to stay or he will deliver these photos to your wife personally.")
            pprint("Make a choice: A: accept the chairmen's offer. B: reject the chairmen's offer still.")
            answer = multiple_choice()
            if answer == 0:
                pprint("The chairmen is very happy with your decision and promised to have a super model to be your personl assistant moving forward. ")
                return 1
            if answer == 1:
                pprint("You admit that you made many mistakes and ignored your family and the people you should care about. You made sure the chairmen know your wife's number and left the room. You went home and confessed to your wife and family, then you also shared the news that you are quitting your job. Your wife and family is very upset, but time only will tell if they will forgive you eventually.")
                return 0
    if answer == 0:
        pprint("The chairmen is very happy with your decision and promised to have a super model to be your personl assistant moving forward. ")
        return 3

def main():
    act2_04()

if __name__ == "__main__":
    main()