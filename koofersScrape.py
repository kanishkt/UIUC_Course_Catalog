import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

br.open("https://www.koofers.com/login")

br.select_form(nr=0)
br.form['email'] = 'sheivingoyal@gmail.com'
br.form['password'] = 'abhisucks'
br.submit()

print br.response().read()