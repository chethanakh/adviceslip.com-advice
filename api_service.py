import os
import requests

def get_advice():
    url = f"https://api.adviceslip.com/advice"

    x = requests.get(url)

    x.raise_for_status()

    return x

