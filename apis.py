import json
import urllib.request
import pprint

def get_insult():
    '''get insult quote from an api online'''
    url = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'
    # print(url)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint.pprint(response_data)
    quote = response_data['insult']
    return quote

def get_math(number):
    '''get a math trivia answer from numbersapi'''
    url = f'http://numbersapi.com/{number}/trivia?json'
    # print(url)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint.pprint(response_data)
    text = response_data['text']
    text = text.split()
    text = " ".join(text[1:])
    return text

def main():
    print(get_insult())
    print(get_math(40))

if __name__ == "__main__":
    main()