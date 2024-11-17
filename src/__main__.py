import requests
from bs4 import BeautifulSoup as bs
import regex as re
import pycuda as pyc
import hashlib as hl
from __checkers__ import basic_check, check_bestbuy, check_walmart, check_amazon
from __database__ import get_connection, create_table, insert_data 



if __name__ == "__main__":
    create_table()
    check_amazon()