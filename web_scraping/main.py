from importlib.metadata import files
from urllib import response
from venv import create
from parsel import Selector

from scraping import read_page_and_return_html, get_number_of_pages, generate_all_catalogue_pages, get_books_in_catalogue_page, generenate_link, query_html_xpath


url_main = 'http://books.toscrape.com/'



html_url_main = read_page_and_return_html(url_main)
response_main = Selector(text=html_url_main)


number_of_pages = get_number_of_pages(response_main)


list_catalogue = generate_all_catalogue_pages(url_main, number_of_pages)
list_catalogue = list_catalogue[0:1]

dict_books_in_catalogue_page = get_books_in_catalogue_page(list_catalogue)

list_links_all_books = generenate_link(url_main, dict_books_in_catalogue_page)
list_links_all_books = list_links_all_books[0:1]

for link in list_links_all_books:
    url = link
    html = read_page_and_return_html(url)
    response = Selector(text=html)
    name = query_html_xpath(response, "//*[@id='content_inner']/article/div/div/h1[1]")
    upc = query_html_xpath(response, "//*[@id='content_inner']/article[1]/table[1]/tbody[1]/tr[1]/td[1]")
    price_exl_tax = query_html_xpath(response, "//*[@id='content_inner']/article[1]/table[1]/tbody[1]/tr[2]/td[1]")
    price_icl_tax = query_html_xpath(response, "//*[@id='content_inner']/article[1]/table[1]/tbody[1]/tr[4]/td[1]")
    tax  = query_html_xpath(response, "//*[@id='content_inner']/article[1]/table[1]/tbody[1]/tr[5]/td[1]")
    stock  = query_html_xpath(response, "//*[@id='content_inner']/article/div/div/p[2]")
    number_of_review = query_html_xpath(response, "//*[@id='content_inner']/article[1]/table[1]/tbody[1]/tr[7]/td[1]")
    rate = query_html_xpath(response, "//*[@id='content_inner']/article/div/div/p[3]")

    dict_data = {
        "name": name,
        "upc": upc,
        "price_exl_tax": price_exl_tax,
        "price_icl_tax": price_icl_tax,
        "tax":tax,
        "stock": stock,
        "number_of_review":number_of_review,
        "rate": rate
    }
for key, value in dict_data.items():
    print(key, value)
        