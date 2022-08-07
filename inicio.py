from cgitb import text
from tabnanny import check
from parsel import Selector
import re
from functions import create_file, generate_links, generate_list_with_urls_catalogue, read_page_and_return_html, infos_current_page, generate_dict_links

url_base = 'http://books.toscrape.com'


soup = read_page_and_return_html(url_base)

response_main = Selector(text=soup)

infos_main_page = infos_current_page(response_main)
main_page = infos_main_page['current_pag']
max_page = infos_main_page['max_pag']

catalogue_page_list = generate_list_with_urls_catalogue(url_base, max_page)


dict = generate_dict_links(catalogue_page_list)

list_all_links = []
for key, value in dict.items():
    for item in value:
        url = f"{url_base}/catalogue/{item}"
        list_all_links.append(url)

print(list_all_links)