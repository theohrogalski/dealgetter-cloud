import requests
from bs4 import BeautifulSoup as bs
import regex as re
import pycuda as pyc
import hashlib as hl
import logging
import scrapy
from scrapy_playwright.page import PageMethod

class Amztest1Spider(scrapy.Spider):
    name = "amztest1"

    def start_requests(self):
        url = 'https://www.amazon.com/deals'
        yield scrapy.Request(url, callback=self.get_deals_list, 
            meta={
                "playwright" : True,
                "playwright_include_page" : True,
                "playwright_page_methods" :[
                        PageMethod('wait_for_selector', 'div#grid-main-container', timeout=0),
                        PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)"),
                    ],
                "playwright_context_kwargs": {"ignore_https_errors": True,},
                "playwright_page_goto_kwargs": {"wait_until": "networkidle",},
                "errback":self.errback,
                }
        )


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


def check_amazon(self) -> bool:
    print()


def check_walmart() -> bool:
    print("Checking Walmart...\n")


def check_bestbuy() -> bool:
    print("Checking Best Buy...\n")
