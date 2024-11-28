import requests
from bs4 import BeautifulSoup as bs
import regex as re
import pycuda as pyc
import hashlib as hl
from __checkers__ import basic_check, check_bestbuy, check_walmart, check_amazon
from __database__ import get_connection, create_table, insert_data 



if __name__ == "__main__":
    basic_check()
    create_table()
    x = 4
    while(x!=0):
        x=int(input("Input which site. \n 1 for amazon \n 2 for bestbuy \n 3 for walmart \n 0 for ext"))

        if(x==1):

            insert_data(check_amazon())
            print("Operations completed. Exiting...")
            continue
        if(x==2) :
            insert_data(check_bestbuy)
            print("Operations completed. Exiting...")

        if(x==3) :
            insert_data(check_walmart)
            print("Operations completed. Exiting...")
        else :
            print("invalid input\n")