from Negotaition import offer, no_deal, yes_deal
from pprint import pprint
from multiple_choice import multiple_choice
import sentiment
from act1 import act1_01,act1_02,act1_03,opening

def name():
        name = input("What is your name? Enter here:")
        print(f'Hi, {name}, welcome to the story!')
        return name

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
        player.wife_affection += 1
    son2 = act1_02()
    player.son_affection += son2
    if son2 > 1:
        player.wife_affection += 1

    print(player)

def main():
    main_story()


if __name__ == '__main__':

    main()