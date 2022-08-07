from cgitb import text
from tabnanny import check
from parsel import Selector
import re
from functions import generate_list_with_urls_catalogue, read_page_and_return_html, infos_current_page, generenate_link, generate_dict_links

url_base = 'http://books.toscrape.com'


soup = read_page_and_return_html(url_base)

response_main = Selector(text=soup)

infos_main_page = infos_current_page(response_main)
main_page = infos_main_page['current_pag']
max_page = infos_main_page['max_pag']

catalogue_page_list = generate_list_with_urls_catalogue(url_base, max_page)
catalogue_page_list= catalogue_page_list[0:1]

dict = generate_dict_links(catalogue_page_list)

print(generenate_link(url_base,dict))