'''improve son's affection'''
from pprint import pprint
import random
import apis

def math_game():
    '''a scenerio that takes place in act 1 that allows you to improve your son affection points'''
    pprint("You sits down to the computer. The screen shows: Welcome to math trivia quiz of for the Sierra Middle School, score 5/10 or above to pass.")
    score = 0
    for i in range(9):
        number = random.randint(10,20)
        text = apis.get_math(number)
        pprint(f"Trivia question: what {text}")
        answer = int(input("Enter your answer here, an integer between 10 and 20:"))
        tries = 1
        if answer == number:
            pprint("Congratulations, you are correct!")
            score += 1
            continue
        else:
            while tries < 3 and answer != number:
                tries += 1
                pprint("You are wrong or you entered an invalid input, try again")
                answer = int(input("Enter your answer here, an integer between 10 and 20:"))
                if answer == number:
                    pprint("Congratulations, you are correct!")
                    score += 1
                    continue
                if tries >= 3:
                    pprint(f"You are wrong, the correct answer is {number} moving on to the next question")
    
    if score >= 5:
        pprint(f"Congratulations you got {score} points, you passed")
        if score >= 7:
            return 2
        return 1
    else:
        pprint(f'Sorry, you did not pass, you only have {score} out of 10 points.')
        return 0

def main():
    math_game()

if __name__ == '__main__':

    main()
