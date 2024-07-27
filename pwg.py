#code exp:  This is my 1st ever project with the help of bro code, code academy, and chatgpt ofc, I used chat gpt to quiz me, and to improve the code I already created.  
#This is nothing but a learning experince for me.
#any who, this is a personal password generator that I created using API random word
#usually pwg have all type of characters that people cant remember, so i thought why not make it to to where people can

import random 
import string
import requests

def get_sets():

    sets = {
        "lowercase" : string.ascii_lowercase, 
        "uppercase" : string.ascii_lowercase,
        "numbers" : string.digits,
        "puncuation" : string.punctuation
               
               }
    return sets

def get_api():
    url = 'https://random-word-api.herokuapp.com/all'
    response = requests.get(url)
    if response.status_code == 200:
