"""Let's scrape basketball-reference!"""
#import BeautifulSoup
import requests
import mechanize
import cookielib
import os
import time
import random

overwrite = False #this flag determines whether the scraper will overwrite files that already have been scraped.

#following br setup code from http://stockrt.github.io/p/emulating-a-browser-in-python-with-mechanize/
# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# User-Agent
br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0'),
                 ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                 ('Accept-Language', 'en-US,en;q=0.5'),
                 ('Accept-Encoding', 'gzip, deflate'),
                 ('Connection', 'keep-alive')]



#let's get all of the player pages
#first, the index of all players

#~7000 player pages... if I want the scraping to take ~1 hr, then I should have 2 requests per second.

if not os.path.exists('scraped-html'):
    os.makedirs('scraped-html')
if not os.path.exists('scraped-html/players'):
    os.makedirs('scraped-html/players')

index_page = br.open('http://www.basketball-reference.com/players/a')
html = index_page.read()
with open('scraped-html/a.html', 'wb') as outfile:
	outfile.write(html)

for letter in 'abcdefghijklmnopqrstuvwxyz':
	print('Scraping {}'.format(letter))
	#pause to make it seem not like a scraper
	time.sleep(0.3 + random.random()*2)
	try:
		br.set_response(index_page)
		index_page = br.follow_link(text=letter.upper())
		html = index_page.read()
		with open('scraped-html/{}.html'.format(letter), 'wb') as outfile:
			outfile.write(html)
	except mechanize._mechanize.LinkNotFoundError:
		print('{} not found'.format(letter))

	links_to_player_pages = br._filter_links(br.links(),url_regex = "/players/./.+")
	for link in links_to_player_pages:
		if overwrite or not os.path.isfile('scraped-html/players/{}.html'.format(link.text)) :
			print("Scraping {}'s player page.".format(link.text))
			time.sleep(0.4)
			player_page = br.follow_link(link)
			html = player_page.read()
			with open('scraped-html/players/{}.html'.format(link.text), 'wb') as outfile:
				outfile.write(html)
		else:
			print("skipping {}'s player page".format(link.text))