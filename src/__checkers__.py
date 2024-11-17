import requests
from bs4 import BeautifulSoup as bs
import regex as re
import pycuda as pyc
import hashlib as hl
import logging
import psycopg



def basic_check() -> bool:
    print("Running checks with requests, bs4 and ppycuda...\n ")
    requ = requests.get("https://google.com")
    requ = bs(requ.text, "html.parser")
    sha=hl.sha256()
    string_hash = sha.hexdigest()

    try:
        with open(f"written_{string_hash}.txt", "w") as file:
            file.write(requ.prettify())
    except:
        return False
    return True

def check_amazon()-> str:
    print("Checking amazon")

    requ = requests.get("https://amazon.com/deals")
    print("requ set 1")
    requ = bs(requ.text, "html.parser")
    print("requ set 2")
    return requ

    
def check_walmart() -> bool:
    print("Checking Walmart...\n")


def check_bestbuy() -> bool:
    print("Checking Best Buy...\n")
