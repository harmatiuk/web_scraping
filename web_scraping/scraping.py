
import requests
import re
from bs4 import BeautifulSoup
from parsel import Selector



def read_page_and_return_html(page_str):
    
    page = requests.get(f"{page_str}")
    html_return = BeautifulSoup(page.content, 'html.parser')
    return str(html_return)

def create_file(folder,file_name, extension, values):
    
    arq_html = open(f'./files/{folder}/{file_name}.{extension}', 'w')
    arq_html.write(str(values))
    arq_html.close()

def query_html_xpath(response, xpath):

    result_xpath = response.xpath(xpath).getall()
    return result_xpath

def finding_largest_integer_in_string(str):

    nums=re.findall("\d+",str)
    return int(max(nums))

def get_number_of_pages(response):
    
    infos_current_pag_xpath="//li[contains(@class, 'current')]"
    infos = query_html_xpath(response ,infos_current_pag_xpath)[0]
    number_of_pages = finding_largest_integer_in_string(infos)
    return number_of_pages

def generate_all_catalogue_pages(url_base, number_of_pages):
    
    list_catalogue = []
    for catalogue_page in range(1, number_of_pages+1):
        page = f"/catalogue/page-{catalogue_page}.html"
        url = f"{url_base}{page}"
        list_catalogue.append(url)
    return list_catalogue

def get_books_in_catalogue_page(catalogue_page_list):

        dict_link = {}
        for item in catalogue_page_list:
            soup = read_page_and_return_html(item)
            response = Selector(text=soup)
            xpath = "//div[contains(@class, 'image_container')]/a/@href"
            pag = re.findall("[0-9]+", item)[0]
            dict_link[f"page_{pag}"]= query_html_xpath(response, xpath)
        return dict_link

def generenate_link(url_base,dict):

    list_all_links = []
    for key, value in dict.items():
        for item in value:
            url = f"{url_base}/catalogue/{item}"
            list_all_links.append(url)
    return list_all_links


def get_books_infos_from_list(list):
 
    return 






