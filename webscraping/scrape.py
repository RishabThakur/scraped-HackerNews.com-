'''
HEllO!!!!
Install These all Modules Before running the code :)
'''


import requests  # it sends HTTP request with python
from bs4 import BeautifulSoup  #Beautiful soup library is used for extracting data from website HTMl content
import pprint # it prettify's the syntax of result
import json

res = requests.get('https://news.ycombinator.com/news') #requesting and getting response

soup = BeautifulSoup(res.text, 'html.parser') # it creates a 'BeautifulSoup' object


links = soup.select('.storylink')  # here ".storylink" is class of the links for which we select it and take all the links..
'''
IMPORTANT NOTE: Go Through BeautifulSoup documentation Its easy to learn ' :-) '
'''
subtext = soup.select('.subtext')
def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99:
        hn.append({'title': title, 'link': href, 'votes': points})
  return sort_stories_by_votes(hn)
 
pprint.pprint(create_custom_hn(links,subtext))

'''
  {{{{{  THANKYOU    }}}}}
'''
