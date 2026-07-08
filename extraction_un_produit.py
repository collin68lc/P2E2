import requests

url = "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"
response = requests.get (url)

from bs4 import BeautifulSoup

import csv


# Extraction des informations souhaitées avec Beautiful Soup
with open("index.html", "r", encoding="utf-8") as file:
   soup = BeautifulSoup(response.text, 'html.parser')


# Extraction code UPC
td = soup.td.string
print("UPC:", td)

# Extraction du titre de la page
title = soup.title.text
print("Titre de la page:", title)


# Extraction prix TTC
price = soup.find_all("td") [3].string
print ("Prix TTC :", price) 

# Extraction prix HT
Price = soup.find_all("td") [2].string
print ("prix HT:", price)

# Disponibilité 
availability = soup.find_all("td") [5].string
print ("disponibilité:", availability)

# description
sub = soup.find('div', class_="content")
description = sub.find_all("p") [3]
print ("description:", description.string)

# image
image = soup.find("div", class_= "item active").find("img")

print("image_url:", image["src"])

# categorie
category = soup.find("ul", class_="breadcrumb")
categories = category.find_all("a") [2]
print("catégorie:", categories.text)

# review rating
review = soup.find_all("td") [6]
print("review_rating:", review.text)



# Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
with open('data.csv', 'w') as fichier_csv:
    fieldnames = ['1', '2']
    writer = csv.DictWriter(fichier_csv, fieldnames=fieldnames)

    writer.writerow({'1': 'product_page_url', '2': 'https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html'})
    writer.writerow({'1': 'universal_ product_code (upc)', '2': '4165285e1663650f'})
    writer.writerow({'1': 'title', '2': 'Sapiens: A Brief History of Humankind'})
    writer.writerow({'1': 'price_including_tax', '2': '£54.23'})
    writer.writerow({'1': 'price_excluding_tax', '2': '£54.23'})
    writer.writerow({'1': 'number_available', '2': 'In stock (20 available)'})
    writer.writerow({'1': 'product_description', '2': 'From a renowned historian comes a groundbreaking narrative of humanityâs creation and evolution'})
    writer.writerow({'1': 'category', '2': 'History'})
    writer.writerow({'1': 'review_rating', '2': '0'})
    writer.writerow({'1': 'image_url', '2': '../../media/cache/ce/5f/ce5f052c65cc963cf4422be096e915c9.jpg'})
