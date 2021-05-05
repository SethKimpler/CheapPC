# Author: Connor Gesner
# Edited: Seth Kimpler

from bs4 import BeautifulSoup

import requests
import json

import os  # for testing


# Function to extract Product Title
def get_title(soup):
    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id": 'productTitle'})

        # Inner NavigatableString Object
        title_value = title.string

        # Title as a string value
        title_string = title_value.strip().replace(',', '')


    except AttributeError:
        title_string = ""

    return title_string


# Function to extract Product Price
def get_price(soup):
    try:
        price = soup.find("span", attrs={'id': 'priceblock_ourprice'}).string.strip().replace('$', '').replace(',', '')

    except AttributeError:

        try:
            # If there is some deal price
            price = soup.find("span", attrs={'id': 'priceblock_dealprice'}).string.strip().replace(',', '').replace('$',
                                                                                                                    '')

        except:
            price = "0"

    return float(price)


# Function to extract Availability Status
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id': 'availability'})
        available = available.find("span").string.strip().replace(',', '')

    except AttributeError:
        available = "Not Available"

    return available


# Function to extract image address
def get_img(soup):
    try:
        img_div = soup.find(id="imgTagWrapperId")

        imgs_str = img_div.img.get('data-a-dynamic-image')  # a string in Json format

        # convert to a dictionary
        imgs_dict = json.loads(imgs_str)
        # each key in the dictionary is a link of an image, and the value shows the size (print all the dictionay to inspect)
        num_element = 0
        first_link = list(imgs_dict.keys())[num_element]

    except AttributeError:
        first_link = "Not Available"

    return first_link


if __name__ == '__main__':

    print('scraping')  # for testing

    # Headers for request
    HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US'})

    # The webpage URL
    URL = "https://www.amazon.com/b?node=284822&ref=sr_nr_n_3"

    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")

    # Fetch links as List of Tag Objects
    links = soup.find_all("a", attrs={'class': 'a-link-normal s-no-outline'})

    # Store the links
    links_list = []

    # Loop for extracting links from Tag Objects
    for link in links:
        links_list.append(link.get('href'))

    # Loop for extracting product details from each link
    # path needs to be relative to highest level function calling it
    File = open("gpu/files/out.csv", "a")
    for link in links_list:

        File = open("gpu/files/out.csv", "a")

        new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)

        new_soup = BeautifulSoup(new_webpage.content, "lxml")

        # Function calls to display all necessary product information
        page = "https://www.amazon.com" + link
        title = get_title(new_soup).replace(',', '')
        price = get_price(new_soup)
        # aval = get_availability(new_soup).replace(',', '')
        img = get_img(new_soup)
        if price != "" and price > 20:
            print("Product Page =", page)
            File.write(f"{page},")
            print("Product Title =", title)
            File.write(f"{title},")
            print("Product Price =", price)
            File.write(f"{price},")
            print("Img =", img)
            File.write(f"{img},\n")
            print()
            print()
        File.truncate(0)  # erases contents of file after writing
        File.close()
