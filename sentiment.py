'''measure user's response based on sentimnet analysis'''
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def natural_language_processing(input):
    '''return the sentiment score of the input'''
    sentence = input
    score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    if score['pos'] > score['neg']:
        return 1
    else:
        return 0

def main():
    natural_language_processing("Son, I am sorry are you okay?")

if __name__ == "__main__":
    main()

