import selenium
import requests
from cgitb import text
from bs4 import BeautifulSoup
from urllib import response
from parsel import Selector
import re




def read_page_and_return_html(page_str):
    
    page = requests.get(f"{page_str}")
    html_return = BeautifulSoup(page.content, 'html.parser')
    return str(html_return)

def create_file(folder,file_name, extension, values):
    
    arq_html = open(f'./files/{folder}/{file_name}.{extension}', 'w')
    arq_html.write(str(values))
    arq_html.close()

def read_file(file):

    with open(f"./files/{file}", 'r') as f:
        content_file = f.read()
    return content_file

def finding_largest_integer_in_string(str):

    nums=re.findall("\d+",str)
    return int(max(nums))

def finding_smallest_integer_in_string(str):

    nums=re.findall("\d+",str)
    return int(min(nums))

def query_html_xpath(response, xpath):

    result_xpath = response.xpath(xpath).getall()
    return result_xpath

def infos_current_page(response):

    infos_checks = {"current_pag":"", "max_pag": ""}
    current_pag_xpath="//li[contains(@class, 'current')]"

    current = query_html_xpath(response, current_pag_xpath)[0]
    current_pag = finding_smallest_integer_in_string(current)
    max_pag = finding_largest_integer_in_string(current)
    infos_checks["current_pag"] = current_pag
    infos_checks["max_pag"] = max_pag

    return infos_checks

def generate_list_with_urls_catalogue(url_base, n_link):

    list_catalogue = []
    for x in range(1,n_link+1):
        page = f"/catalogue/page-{x}.html"
        url = f"{url_base}{page}"
        list_catalogue.append(url)
    return list_catalogue

def generate_file_based_on_list(list, extension ,folder):

    for item in list:
        soup = read_page_and_return_html(item)
        pag = re.findall("[0-9]+", item)[0]
        name = f"page-{pag}"
        create_file(folder, name, extension, soup)




