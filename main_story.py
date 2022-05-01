from Negotaition import offer, no_deal, yes_deal
from act2 import act2_01,act2_02,act2_04,act2_03
from act1 import act1_01,act1_02,opening,act1_03
from pprint import pprint

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

def act3_preview():
    '''A preview of Act 3'''
    pprint("""If your son points is highest, you will go on trip with son after divorsing your wife. If your wife points is highest, you will go on honeymoon with your wife. If your comapany points is the highest, you will do very well in company but your family problems are exacerbated. """)

def main_story():
    '''This the the function that support the main story line'''
    son1 = 0
    son2 = 0
    wife1 = 0
    wife2 = 0
    company1 = 0
    company2 = 0
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
    son1 = int(act1_01())
    if son1 ==0:
        player.son_affection -= 1
    else:
        player.son_affection += 1
        player.wife_affection += 1
    son2_1 = act1_02()
    if son2_1 == 1:
        son2 = int(act1_03())
    player.son_affection += son2
    if son2 > 1:
        player.wife_affection += 1
    company1 = int(act2_01())
    if company1 == 0:
        player.company_affection += 1
    wife1 = int(act2_02())
    player.wife_affection += wife1
    if wife1 == 0:
        wife2 = act2_03()
        player.wife_affection += wife2
    company2 = int(act2_04())
    if company2 == 0:
        player.wife_affection += 1
        player.son_affection += 1
        player.company_affection -= 1
    player.company_affection += company2
    print(player)
    act3_preview()

def main():
    main_story()

if __name__ == "__main__":
    main()