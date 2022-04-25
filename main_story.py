from Negotaition import offer, no_deal, yes_deal
from pprint import pprint
from multiple_choice import multiple_choice

def name():
        name = input("What is your name? Enter here:")
        print(f'Hi, {name}, welcome to the story!')
        return name

def opening():
    pprint("""You are the CFO of Colson Group; you are currently striking a deal to purchase an manufacturing plant. The seller offer is $1500000, but you believe the value of manufacturing plant is only about $1000000, and your company do not wish to pay more than $250000 in premium. You were given $1250000, you can't pay more than that. Your latest offer was $900000. Seller says: $1450000 is our last offer. If you do not take it, then we will look for someone else.""")

class Player:
    '''This class is created for the purpose of keeping points for the interactive story'''
    def __init__(self,name):
        self.name = name
        self.company_affection = 0
        self.son_affection = 0
        self.wife_affection = 0
    
    def __str__(self):
        '''return a summary of the points the player have.'''
        return f'Hi {self.name}, you currently have {self.son_affection} son affection points and {self.wife_affection} wife affection points and {self.company_affection} company affection points.'


def act1_01():
    pprint('''After you finished your work, you walk on the helipad and boards your luxurious helicopter home. You enjoy a helicopter ride cruising down the city lights and busy streets and suddenly arrives at a mansion on the cliff of a mountain hill. After you landed, you saw your family gathering around a table and singing Happy Birthday to your son. You forgot it is his birthday today which your wife reminded you this morning.''')
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

def main_story():
    '''This the the function that support the main story line'''
    player = Player(name())
    opening()
    deal = offer()
    if deal == 1:
        yes_deal()
        player.company_affection +=1
    else:
        deal2 = no_deal()
        if deal2 == 1:
            player.company_affection += 1
        else:
            player.company_affection -= 1
    son1 = act1_01()
    if son1 ==0:
        player.son_affection -= 1
    else:
        player.son_affection += 1
    print(player)

def main():
    main_story()


if __name__ == '__main__':

    main()