import requests
from bs4 import BeautifulSoup

#souper class
class Souper():
    #global vars
    __url = ''
    __res = ''
    __soup = None
    __payload = None
    __last_url = ''

    #func get_res
    #returns response object
    def get_res(self):
        return self.__res

    #func get_url
    #returns the initial scrape url
    def get_url(self):
        return self.__url
    
    #func get_payload
    #returns the current payload
    def get_payload(self):
        return self.__payload

    #func get_last_url
    #returns the last redirected url
    def get_last_url(self):
        return self.__last_url

    #func get_soup
    #returns bs4 soup object
    def get_soup(self):
        if len(self.__res.text) != 0:
            self.__soup = BeautifulSoup(self.__res.text, 'html.parser')
            return self.__soup, self.__last_url
        else:
            return None

    #Souper class
    #constructor
    def __init__(self, url, payload=None):
        self.__url = url
        if payload == None:
            self.__res = requests.get(url)     #set the res as response text
            self.__last_url = self.get_res().url    #set last_url as the last redirected url
        else:
            self.__res = requests.get(url, params=payload)    #set the res as response text
            self.__last_url = self.get_res().url    #set last_url as the last redirected url
