import requests
from bs4 import BeautifulSoup as bs
import regex as re
import pycuda as pyc
import hashlib as hl
from __checkers__ import basic_check, check_amazon, check_bestbuy, check_walmart, Amztest1Spider
if __name__ == "__main__":
    if basic_check()==True:
        print("Basic check passed.\n")
    else : 
        exit(1)
    done=False
    while(done==False) :
        print("1. Check Amazon\n2. Check Walmart\n3. Check Best Buy\n4. Exit\n")
        choice = int(input("Enter your choice: "))
        if choice==1:
            p = Amztest1Spider()
            
            if p.start_requests()==True:
                print("Amazon check passed.\n")
            else:
                print("Amazon check failed.\n")
        elif choice==2:
            if check_walmart()==True:
                print("Walmart check passed.\n")
            else:
                print("Walmart check failed.\n")
        elif choice==3:
            if check_bestbuy()==True:
                print("Best Buy check passed.\n")
            else:
                print("Best Buy check failed.\n")
        elif choice==4:
            done=True
        else:
            print("Invalid choice.\n")