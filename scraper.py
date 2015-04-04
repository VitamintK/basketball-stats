"""Let's scrape basketball-reference!"""
#import BeautifulSoup
import requests
import mechanize
import cookielib

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

page = br.open('http://www.basketball-reference.com/players/a/')
html = page.read()
with open('scraped-html/A.html', 'wb') as outfile:
    outfile.write(html)

