import json
from api_service import *


def get_single_advice():
    try:
        advice=get_advice().json().get('slip') 
        if len(advice['advice']) < 30:
            print(advice['advice'])
        else:
            print("Your Advice too long to display here")
    except requests.exceptions.RequestException as e:
        print(e)

def log_100_advice():
    i = 0
    advice_list = {'non_c':[],'c':[]}
    while i < 100:
        try:
            advice=get_advice().json().get('slip')
            advice_str=advice['advice']

            advice_word=advice_str.split()

            if advice_word[0].lower().find("c") != -1 or advice_word[1].lower().find("c") != -1:
                advice_list['c'].append(advice_str)
            else:
                advice_list['non_c'].append(advice_str)
            i+=1
            print("Wrote "+str(i))
        except requests.exceptions.RequestException as e:
            print(e)
    
    print("String file Writing")
    
    json_object = json.dumps(advice_list, indent=4)
    with open("advice.json", "w") as outfile:
        outfile.write(json_object)
    
    print("file Wrote")

    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("C Words:")
    
    print(advice_list['c'])



get_single_advice()
# log_100_advice()