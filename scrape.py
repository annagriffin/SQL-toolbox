import requests
from bs4 import BeautifulSoup

#TODO: install requests and beautiful soups


url = "http://books.toscrape.com/"

html_text = requests.get(url)
soup = BeautifulSoup(html_text.text, "html.parser")

# print(soup.prettify())
section = soup.section
print(section)


def stringNumToInt(strNum):
    """
    Dictionary mapping word representation of numbers to ints
    """

    # to normalize
    strNum = strNum.lower()

    numDict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5
    }

    return numDict[strNum]

"""
Book Example:
fields:
> title
> rating
> price
> status
> url address for the page description
"""

products = section.find_all("article", {"class": "product_pod"})

for product in products:

  link = product.select('a')

  price = product.find("p",'price_color').text

  rating = product.p["class"][1]
  rating_int = stringNumToInt(rating.lower())

  availability = product.find("p", {"class": "availability"}).text
  availability = availability.strip()
  title = product.h3.a["title"]






