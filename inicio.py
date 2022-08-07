from tabnanny import check
from parsel import Selector
import re
from functions import create_file, generate_list_with_urls_catalogue, read_page_and_return_html, infos_current_page

url_base = 'http://books.toscrape.com'


soup = read_page_and_return_html(url_base)

response = Selector(text=soup)

infos_main_page = infos_current_page(response)
main_page = infos_main_page['current_pag']
max_page = infos_main_page['max_pag']

catalogue_page_list = generate_list_with_urls_catalogue(url_base, max_page)


for item in catalogue_page_list:
    soup = read_page_and_return_html(item)
    pag = re.findall("[0-9]+", item)[0]
    name = f"page-{pag}"
    create_file(name, "html", soup)
