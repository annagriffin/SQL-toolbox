import requests
from bs4 import BeautifulSoup

import sqlite3

def createSoup(urlAddress):
  html_text = requests.get(urlAddress)
  soup = BeautifulSoup(html_text.text, "html.parser")
  return soup


soup = createSoup('http://quotes.toscrape.com/')
# print(soup.prettify())



# get list of all quotes on page
# each quote is contained in a div with the "quote" class
quotes = soup.find_all("div", {"class": "quote"} )




def makeOneQuote(content):

  quote = {}

  text = content.find("span", "text").text
  author = content.find("small", "author").text

  author_about = content.find("a")["href"]

  all_tags = content.find("meta", "keywords").findChildren()

  tags = []
  for tag in all_tags:
    tags.append((tag.text, tag["href"]))

  return makeDict(text, author, author_about, tags)


def makeDict(text, author, author_about, tags):

  quote = {
    "text": text,
    "author": author,
    "author_about": author_about,
    "tags": tags
  }

  return quote


for each in quotes:
  print(makeOneQuote(each))
  print("________________________________-")



def connectToDatabase(dbFileName):
  conn = sqlite3.connect(dbFileName)
  cursor = conn.cursor()
  print("opened database successfully")



connectToDatabase('my_database.db')
"""
<div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
<span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
<span>by <small class="author" itemprop="author">Albert Einstein</small>
<a href="/author/Albert-Einstein">(about)</a>
</span>
<div class="tags">
            Tags:
            <meta class="keywords" content="change,deep-thoughts,thinking,world" itemprop="keywords">
<a class="tag" href="/tag/change/page/1/">change</a>
<a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
<a class="tag" href="/tag/thinking/page/1/">thinking</a>
<a class="tag" href="/tag/world/page/1/">world</a>
</meta></div>
</div>
"""




"""CREATE TABLE quotes (
  text TEXT,
  author TEXT,
  author_about TEXT,
  tags TEXT,
  tags_href TEXT
)"""



