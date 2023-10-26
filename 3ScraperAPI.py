import re
from selenium import webdriver
import time
import requests


def get_final_url(url):
    try:
       
        api_key = '7e5a61baffa35ef6acb6429577ceec33'
        api_url = f'http://api.scraperapi.com?api_key={api_key}'

        
        payload = {'url': url}
        response = requests.get(api_url, params=payload)

        if response.status_code == 200:
            final_url = response.text
        else:
            final_url = None

        return url, final_url

    except Exception as e:
        return url, f"Terjadi kesalahan: {str(e)}"


with open('link2.txt', 'r') as file:
    for line in file:
        url = line.strip()
        original_url, final_url = get_final_url(url)
        
        if final_url:
           
            match = re.search(r'var baseUrl = "(.*?)";\s+var currentUrl = "(.*?)";\s+var currentLocale = "(.*?)";\s+var environment = "(.*?)";\s+window.bugsnagKey = "(.*?)";', final_url)
            if match:
                baseUrl, currentUrl, currentLocale, environment, bugsnagKey = match.groups()
                print(f"Origin URL: {original_url}\nbaseUrl: {baseUrl}\ncurrentUrl: {currentUrl}\ncurrentLocale: {currentLocale}\nenvironment: {environment}\nbugsnagKey: {bugsnagKey}\n")
        else:
            print(f"Origin URL: {original_url}\nNo redirects.\n")


