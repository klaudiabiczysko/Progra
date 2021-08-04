from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

def wiki_query(name):
  url = requests.get(f"https://en.wikipedia.org/wiki/{name}")
  soup = BeautifulSoup(url.text, 'html.parser')
  several = False
  for paragraph in soup.find_all("p"):
    if "Other reasons this message may be displayed:" in paragraph.text:
      soup = None
      break
    elif "may refer to:" in paragraph.text:
      soup = None
      several = True # There are several wikipedia pages for this term.
      break

  try:
    for paragraph in soup.find_all("p"):
      print(paragraph.text)
  except AttributeError:
      if several:
          print ("You need to be more specific. Your search term seems to have several meanings.")
      else:
          print("The page does not exist.")

if __name__ == "__main__":
  import sys
  from sys import stdin, stderr
  entry = sys.argv[1]
  wiki_query(entry)
