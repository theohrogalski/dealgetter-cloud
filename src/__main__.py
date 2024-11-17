import requests
from bs4 import BeautifulSoup as bs
import regex as re
import pycuda as pyc
import hashlib as hl
from __checkers__ import basic_check, check_amazon, check_bestbuy, check_walmart
if __name__ == "__main__":
    x=True
    while(x==True):
        if(basic_check()==True):
            print("All checks passed successfully.\n")
            continue
        else:
            print("Error in checks.\n")
            x=False
        if (y==0) :
           y=input("Press 1 to check Amazon, 2 to check Walmart, 3 to check Best Buy, 4 to exit: ")
        if (y==1):
            check_amazon()
        elif (y==2):
            check_walmart()
        elif (y==3):
            check_bestbuy()
        elif (y==4):
            x=False
        else :
            print("Invalid input.\n")
            x=False