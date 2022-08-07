from tabnanny import check
from parsel import Selector
import re
from functions import create_file, generate_list_with_urls_catalogue, read_page_and_return_html, infos_current_page, generate_file_based_on_list

url_base = 'http://books.toscrape.com'


soup = read_page_and_return_html(url_base)

response = Selector(text=soup)

infos_main_page = infos_current_page(response)
main_page = infos_main_page['current_pag']
max_page = infos_main_page['max_pag']

catalogue_page_list = generate_list_with_urls_catalogue(url_base, max_page)

generate_file_based_on_list(catalogue_page_list, "html", "html_catalogue")

