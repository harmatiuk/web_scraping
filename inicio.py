from tabnanny import check
from parsel import Selector
from functions import generate_list_with_urls_catalogue, read_page_and_return_html, infos_current_page

url_base = 'http://books.toscrape.com'


soup = read_page_and_return_html(url_base)

response = Selector(text=soup)

infos_main_page = infos_current_page(response)
main_page = infos_main_page['current_pag']
max_page = infos_main_page['max_pag']

print(generate_list_with_urls_catalogue(url_base, max_page))